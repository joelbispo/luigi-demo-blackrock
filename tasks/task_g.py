import luigi

from tasks.task_e import TarefaE
from tasks.task_f import TarefaF
from util.cronometro import cronometro


class TarefaG(luigi.Task):

    def requires(self):
        return [TarefaE(), TarefaF()]

    def run(self):
        cronometro(5)
        with self.output().open('w') as log:
            log.write('Oi, Arena, eu terminei')

    def output(self):
        return luigi.LocalTarget(f'C:\\temp-luigi\\{self.__class__.__name__}.txt')