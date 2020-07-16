import luigi

from tasks.task_d import TarefaD
from util.cronometro import cronometro


class TarefaF(luigi.Task):

    def requires(self):
        return [TarefaD()]

    def run(self):
        cronometro(5)
        with self.output().open('w') as log:
            log.write('Oi, Arena, eu terminei')

    def output(self):
        return luigi.LocalTarget(f'C:\\temp-luigi\\{self.__class__.__name__}.txt')