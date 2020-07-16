import luigi

from util.cronometro import cronometro


class TarefaA(luigi.Task):

    def run(self):
        cronometro(5)
        with self.output().open('w') as log:
            log.write('Oi, Arena, eu terminei')

    def output(self):
        return luigi.LocalTarget(f'C:\\temp-luigi\\{self.__class__.__name__}.txt')