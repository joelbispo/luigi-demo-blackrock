import luigi

from tasks.task_a import TarefaA
from tasks.task_b import TarefaB
from tasks.task_c import TarefaC
from util.cronometro import cronometro


class TarefaD(luigi.Task):

    def requires(self):
        return [TarefaA(), TarefaB(), TarefaC()]

    def run(self):
        cronometro(5)
        with self.output().open('w') as log:
            log.write('Oi, Arena, eu terminei')

    def output(self):
        return luigi.LocalTarget(f'C:\\temp-luigi\\{self.__class__.__name__}.txt')