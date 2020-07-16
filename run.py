import luigi


from tasks.task_g import TarefaG

if __name__ == '__main__':
    luigi.build([TarefaG()])