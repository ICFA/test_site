from django.db import models

class Cpu_Utilization(models.Model):
    curr_util = models.CharField(max_length = 5)

    def __str__(self):
        util = self.curr_util
        return f'{util}'