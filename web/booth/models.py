from django.db import models
import datetime
from django.db.models import Avg, Count, Min, Sum, F, Q
from django.db.models import Value, IntegerField
from django.db.models.functions import Coalesce

# from player.models import Player

# Create your models here.
class BoothRequirement(models.Model):
    def __str__ (self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    health_score = models.IntegerField(default=0)
    skill_score = models.IntegerField(default=0)
    growth_score = models.IntegerField(default=0)
    relationship_score = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def check_player(self, player):
        failed_list = []
        player_scores = player.get_scores()
        # for score in ['health_score', 'skill_score', 'growth_score', 'relationship_score', 'money']:
        #     print(score, datetime.datetime.now())
        #     if player_scores[score] < getattr(self, score):
        #         failed_list.append(score)
        return failed_list


class Booth(models.Model):
    def __str__(self):
        
        return f"{self.id[:2]} - {self.name}"

    def get_requirements(self):
        result_dict = {
            'health_score': self.health_score,
            'skill_score': self.skill_score,
            'growth_score': self.growth_score,
            'relationship_score': self.relationship_score,
            'money': self.money
        }
        return result_dict

    def check_player(self, player):
        failed_list = []
        player_scores = player.get_scores()
        for score in ['health_score', 'skill_score', 'growth_score', 'relationship_score', 'money']:
            print(score)
            if player_scores[score] < getattr(self, score, 0):
                failed_list.append(score)
        return failed_list

    id = models.CharField(max_length=10, primary_key=True)
    booth_in_charge = models.ForeignKey(
        'account.User', 
        related_name='booth_in_charge', 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )
    booth_admins = models.ManyToManyField('account.User', related_name='booth_admins', blank=True)
    name = models.CharField(max_length=50)
    # score_options = models.ManyToManyField(BoothScoring, related_name='booth_scores', blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    health_score = models.IntegerField(blank=True, null=True, verbose_name='健康分數')
    skill_score = models.IntegerField(blank=True, null=True, verbose_name='技能分數')
    growth_score = models.IntegerField(blank=True, null=True, verbose_name='成長分數')
    relationship_score = models.IntegerField(blank=True, null=True, verbose_name='關係分數')
    money = models.IntegerField(blank=True, null=True, verbose_name='金錢')
    academic_level = models.IntegerField(blank=True, null=True, verbose_name='學歷')
    steps = models.IntegerField(blank=True, null=True)


class BoothScoring(models.Model):
    def __str__(self):
        return self.name
    #     if self.active: 
    #         return self.name 
    #     else:
    #         return self.name + ' (inactive)'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, verbose_name="攤位")
    health_score = models.IntegerField(blank=True, null=True, default=0, verbose_name='健康分數')
    skill_score = models.IntegerField(blank=True, null=True, default=0, verbose_name='技能分數')
    growth_score = models.IntegerField(blank=True, null=True, default=0, verbose_name='成長分數')
    relationship_score = models.IntegerField(blank=True, null=True, default=0, verbose_name='關係分數')
    money = models.IntegerField(blank=True, null=True, default=0, verbose_name='金錢')
    academic_level = models.IntegerField(blank=True, null=True, default=0, verbose_name='學歷')
    steps = models.IntegerField(blank=True, null=True, default=0, verbose_name='步數')
    flat = models.IntegerField(blank=True, null=True, default=0, verbose_name='樓宇')
    record_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="時間")
    active = models.BooleanField(default=True)


class Participation(models.Model):
    def __str__(self):
        return "{} - {} at {}".format(self.booth.name, self.player.user.get_id(), self.record_time.strftime("%Y%m%d %H:%M:%S"))

    def get_time(self):
        return self.record_time.strftime("%d/%m %H:%S")
    
    id = models.AutoField(primary_key=True)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, verbose_name="攤位")
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE, verbose_name="玩家")
    record_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="時間")
    score = models.ForeignKey(BoothScoring, on_delete=models.CASCADE, verbose_name="分數")
    remarks = models.TextField(max_length=1000, null=True, blank=True, verbose_name="評語")
    marker = models.ForeignKey('account.User', on_delete=models.CASCADE, verbose_name="評分員")

class Transaction(models.Model):
    def __str__(self):
        if self.type == 'pay':
            return f'付款${self.money}予玩家{self.player.user.id}'
        if self.type == 'receive':
            return f'從玩家{self.player.user.id}收取${self.money}'
        if self.type == 'deposit':
            return f'玩家{self.player.user.id}存款${self.money}'
        if self.type == 'withdrawal':
            return f'玩家{self.player.user.id}提款${self.money}'
        return False

    def get_time(self):
        return self.record_time.strftime("%d/%m %H:%S")
        
    def get_amount(self):
        if self.type == 'pay':
            return self.money
        else:
            return self.money * -1

    @staticmethod
    def get_player_transactions(player):
        player_trx = Transaction.objects.filter(player=player)
        pay = Coalesce(Sum('money', filter=Q(type='pay')), Value(0))
        receive = Coalesce(Sum('money', filter=Q(type='receive')), Value(0)) 
        deposit = Coalesce(Sum('money', filter=Q(type='deposit')), Value(0))
        withdrawal_money = Coalesce(
            Sum(F('money') * (1 + F('interest_rate')), output_field=IntegerField(), filter=Q(type='withdrawal')), Value(0)
        )
        withdrawal_deposit = Coalesce(Sum(F('money'), filter=Q(type='withdrawal')), Value(0))
        return player_trx.aggregate(
            cash = pay - receive - deposit + withdrawal_money,
            deposit = deposit - withdrawal_deposit,
        )
    id = models.AutoField(primary_key=True)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, verbose_name="攤位")
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE, verbose_name="玩家")
    type = models.CharField(
        max_length=10, 
        choices=(
            ('pay', '付款'), 
            ('receive', '收款'),
            ('deposit', '存款'),
            ('withdrawal', '提款'),
        )
        , verbose_name="交易類型"
    )
    record_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="時間")
    money = models.IntegerField(verbose_name="金錢", default=0)
    interest_rate = models.FloatField(verbose_name='利率', default=0)
    remarks = models.TextField(max_length=1000, null=True, blank=True, verbose_name="備註")
    marker = models.ForeignKey('account.User', on_delete=models.CASCADE, verbose_name="評分員")


class BoothTraffic(models.Model):
    def is_participated(self):
        return Participation.objects.filter(
            player=self.player,
            booth=self.booth
        ).exists()

    # user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE)
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    record_time = models.DateTimeField(auto_now_add=True, blank=True)
