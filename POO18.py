from mysql import connector
from logging import info, getLogger, basicConfig, DEBUG
from datetime import date
from pathlib import Path
from os import makedirs
from tkinter import Tk, Label, font, Button, Entry, PhotoImage, messagebox, Toplevel, StringVar, OptionMenu


class MetaClassSingleton(type):
    '''
    -> Classe que serve como metaclasse para a classe 'BancoDeDados', permitindo que a mesma seja instanciada uma única
     vez
    '''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Interface(metaclass=MetaClassSingleton):
    '''
    -> Classe que permite ser instanciada uma única vez, responsável pelas iterações e interface com o cliente.
    '''

    def bt_host(self):
        '''
        -> Método para capturar o nome do host do banco de dados e atribuir o comando para capturar o nome do usuário
         do mesmo.
        '''
        self.host = self.name_entry.get()
        logger.info(f'HOST: {self.host}')
        self.name_entry.delete(first=0, last=(len(self.host)))
        self.bt_connect['command'] = super(BancoDeDados, self).bt_user
        self.label_name['text'] = 'Digite abaixo o nome do USUARIO que deseja acessar'

    def bt_user(self):
        '''
        -> Método para capturar o nome do usuário do banco de dados e atribuir o comando para capturar a senha do mesmo.
        '''

        self.user = self.name_entry.get()
        logger.info(f'USER: {self.user}')
        self.name_entry.delete(first=0, last=len(self.user))
        self.bt_connect['text'] = 'Conectar'
        self.bt_connect['command'] = super(BancoDeDados, self).bt_password
        self.label_name['text'] = 'Digite abaixo a SENHA'
        self.name_entry['show'] = '*'

    def bt_password(self):
        '''
        -> Método para capturar a senha do banco de dados e iniciar a conexão.
        '''

        self.password = self.name_entry.get()
        logger.info(f'PASSWORD: {self.password}')
        self.label_name['text'] = 'Conectando ao banco de dados MySQL...'
        super(BancoDeDados, self).connect()

    def connect(self):
        '''
        -> Método para conectar a instância do objeto ao MySQL e mostrar os bancos de dados disponíveis.
        '''

        try:
            self.database = ''
            super(BancoDeDados, self).connector()
        except Exception as e:
            logger.exception(e)
            super(BancoDeDados, self).exception_error()
        else:
            logger.info('Conexão com o MySQL realizada com sucesso! STATUS: CONECTADO')
            self.label_name['text'] = f'STATUS: CONECTADO \nDigite o nome do banco de dados que deseja acessar:'
            self.bt_connect['command'] = super(BancoDeDados, self).bt_database
            self.name_entry['show'] = ''

            self.cursor = self.con.cursor()
            self.cursor.execute('show databases;')
            databases = self.cursor.fetchall()
            self.con.close()

            self.text_label = f"\n\n{'-' * 35}\nBanco de dados disponíveis \n{'-' * 35}\n"
            if len(databases) == 0:
                self.text_label += 'Nenhum banco de dados disponível!'
            else:
                for database in databases:
                    self.text_label += str(database).replace("'",'').replace('(', '').replace(')', '\n').replace(',',
                                                                                                                 '')

            self.label_welcome['text'] = self.text_label
            self.label_welcome['font'] = self.font_text
            self.label_welcome['height'] = '10'
            self.label_welcome.pack(side='top', anchor='s')

            self.label_online = Label(self.window, font=self.font_text, text='Opções..', bg='grey11', fg='white')
            self.label_online.place(x=0, y=0, relwidth=0.2, relheight=0.2)
            self.bt_create = Button(self.window, text='Criar', font='Times', width=10,
                                    command=super(BancoDeDados, self).bt_create)
            self.bt_create.place(x=60, y=100)

            self.bt_delete = Button(self.window, text='Excluir', font='Times', width=10,
                                    command=super(BancoDeDados, self).bt_delete)
            self.bt_delete.place(x=60, y=140)

            self.bt_reset = Button(self.window, text='Reiniciar', font='Times', width=10,
                                   command=super(BancoDeDados, self).bt_reset)
            self.bt_reset.place(x=60, y=180)

            self.bt_disconnect = Button(self.window, text='Desconectar', command=super(BancoDeDados, self).disconnect,
                                        width=10, font='Times')
            self.bt_disconnect.place(x=60, y=220)

    def bt_database(self):
        '''
        -> Método para capturar o nome do banco de dados e atribuir o método de conexão ao botão.
        '''

        self.database = self.name_entry.get()
        logger.info(f'DATABASE: {self.database}')
        super(BancoDeDados, self).bt_connect_database()

    def bt_connect_database(self):
        '''
        -> Método para conectar a um banco de dados e mostrar as tabelas disponíveis.
        '''

        try:
            super(BancoDeDados, self).connector()
        except Exception as e:
            logger.exception(e)
            super(BancoDeDados, self).exception_error()
        else:
            logger.info(f'Conexão com o banco de dados "{self.database}" realizada com sucesso! STATUS: CONECTADO')
            self.label_name['text'] = f'STATUS: CONECTADO \nDigite o nome da tabela que deseja acessar:'
            self.bt_connect['command'] = super(BancoDeDados, self).bt_connect_table

            self.cursor = self.con.cursor()
            self.cursor.execute('show tables;')
            tables = self.cursor.fetchall()
            self.con.close()

            self.text_label = f"\n\n{'-' * 40}\nTabelas disponíveis em {self.database} \n{'-' * 40}\n"
            if len(tables) == 0:
                self.text_label += 'Nenhuma tabela existente!'
            else:
                for table in tables:
                    self.text_label += str(table).replace("'", '').replace('(', '').replace(')', '\n').replace(',', '')
            self.label_welcome['text'] = self.text_label
            self.name_entry.delete(first=0, last=len(self.name_entry.get()))

            self.bt_create['command'] = super(BancoDeDados, self).bt_create_table

    def bt_connect_table(self):
        '''
        -> Método responsável por mostrar os registros da tabela e aguardar por uma iteração.
        '''

        self.table = self.name_entry.get()
        try:
            super(BancoDeDados, self).connector()
        except Exception as e:
            logger.exception(e)
            super(BancoDeDados, self).exception_error()
        else:
            logger.info(f'Acesso aos registros da tabela "{self.table}" realizada com sucesso! STATUS: CONECTADO')
           #Abrir nova janela principal com os registros da tabela e interações.

    def disconnect(self):
        '''
        -> Método para desconectar a instância do objeto ao banco de dados.
        '''

        logger.info('Conexão com o banco de dados finalizada com sucesso! STATUS: DESCONECTADO')
        self.con.close()
        self.label_name['text'] = 'STATUS: DESCONECTADO'
        self.bt_connect['command'] = lambda: self.window.destroy()
        self.bt_connect['text'] = 'Sair'
        self.bt_connect['width'] = '10'
        self.name_entry.destroy()

    def bt_reset(self):
        '''
        -> Método para reinicializar a aplicação e fazer uma nova conexão.
        '''

        self.window.destroy()
        BancoDeDados()

    def bt_delete(self):
        '''
        -> Método para excluir um banco de dados ou uma tabela e retornar a estado anterior.
        '''

        msg = 'Operação irreversível! Todos os dados serão perdidos a não ser que tenha feito um dump antes. Deseja ' \
              'apagar o banco de dados mesmo assim?'
        condition = messagebox.askyesno(title='Tem certeza?', message=msg)
        database = self.name_entry.get()
        if condition:
            try:
                super(BancoDeDados, self).connector()
                self.cursor = self.con.cursor()
                self.cursor.execute(f'drop database {database};')
                self.name_entry.delete(first=0, last=len(self.name_entry.get()))
            except Exception as e:
                logger.exception(e)
                super(BancoDeDados, self).exception_error()
            else:
                logger.info(f'Banco de dados "{database}" excluído com sucesso!')
                super(BancoDeDados, self).connect()

    def bt_create(self):
        '''
        -> Método responsável pela criação de banco de dados e tabelas.
        '''

        database = self.name_entry.get()
        msg = f'Deseja criar o banco de dados "{database}"?'
        condition = messagebox.askyesno(title='Criar Banco de Dados?', message=msg)
        if condition:
            try:
                super(BancoDeDados, self).connector()
                self.cursor = self.con.cursor()
                self.cursor.execute(f'create database {database} default char set utf8 default collate utf8_general_ci;')
                self.name_entry.delete(first=0, last=len(self.name_entry.get()))
            except Exception as e:
                logger.exception(e)
                super(BancoDeDados, self).exception_error()
            else:
                logger.info(f'Banco de dados {database} criado com sucesso!')
                super(BancoDeDados, self).connect()

    def bt_create_table(self):
        '''
        -> Método para inicializar a criação de uma nova tabela, dando ao usuário a opção de informar quantas colunas a
         tabela vai ter.
        '''

        table = self.name_entry.get()
        msg = f'Deseja criar a tabela com o nome "{table}"?'
        condition = messagebox.askyesno(title='Criar tabela?', message=msg)
        if condition:
            try:
                super(BancoDeDados, self).connector()
            except Exception as e:
                logger.exception(e)
                super(BancoDeDados, self).exception_error()
            else:
                logger.info(f'Inicializando a criação da tabela "{table}"')
                self.window_table = Toplevel()
                self.window_table.title(f"Criando tabela {table}...")
                self.window_table.geometry('600x230+400+220')
                self.window_table.resizable(False, False)
                self.window_table.transient(self.window)
                self.window_table.focus_force()
                self.window_table.grab_set()
                self.window_table['bg'] = "DarkOrange"

                self.lb_title = Label(self.window_table,
                                 text='Digite a quantidade de colunas que deseja ter \nem sua nova tabela: ',
                                 bg='DarkOrange', font=font.Font(family='Ubuntu', size=15, weight='bold'), height=5,
                                 fg='white')
                self.lb_title.pack(side='top')
                self.entry_table = Entry(self.window_table, width=6, font='Ubuntu', justify='center')
                self.entry_table.place(x=278, y=110)
                self.bt_create_columns = Button(self.window_table, text="Confirmar", font="Times",
                            command=super(BancoDeDados, self).bt_create_columns)
                self.bt_create_columns.place(x=270, y=160)

    def bt_create_columns(self):
        '''
        -> Método responsável por receber os nomes de cada coluna da tabela.
        '''
        num_columns = self.entry_table.get()
        self.entry_table.delete(first=0, last=len(num_columns))
        self.entry_table['width'] = 20
        self.entry_table.place(x=70, y=110)

        self.lb_title['text'] = 'Digite o nome da {n}ª coluna e escolha o seu formato:'
        list_type = ['SELECIONE...', 'Texto Grande', 'Texto (abcd...)', 'Número inteiro (1234)', 'Número Real (3,141)',
                     'Data (AAAA-MM-DD)',]
        self.stringvar = StringVar(self.window_table)
        self.stringvar.set(list_type[0])
        types = OptionMenu(self.window_table, self.stringvar, *list_type)
        types.config(width=20)
        types.place(x=360, y=105)

        self.bt_create_columns['command'] = super(BancoDeDados, self).columns_items
        self.list_columns = list()

    def columns_items(self):
        '''
        -> Método para guardar o nome e o formato da coluna.
        '''
        if self.stringvar.get() == 'SELECIONE...':
            messagebox.showinfo(title='Formato inválido!', message='Selecione o formato da coluna!')
        elif self.stringvar.get() == 'Texto Grande':
            self.list_columns.append(self.entry_table.get())
            self.list_columns.append('Text')
            messagebox.showinfo(title='Coluna armazenada com sucesso!',
                                message=f'Coluna armazenada com as seguintes informações: \n\nNome: '
                                        f'{self.entry_table.get()} \nTipo: {self.stringvar.get()}')
        elif self.stringvar.get() == 'Texto (abcd...)':
            varchar = Toplevel()
            varchar.title('Tamanho do campo')
            varchar.geometry('300x150+550+270')
            varchar.focus_force()
            varchar.grab_set()
            varchar.resizable(False, False)
            varchar['bg'] = "Navy"

            font_varchar = font.Font(family='Ubuntu', size=10, weight='bold')
            lb_varchar = Label(varchar, text='Digite a quantidade máxima de caracteres \nque pode existir no campo'
                                             ' da coluna:', height=4, bg='Navy', fg='white', font=font_varchar)
            lb_varchar.pack(side='top')
            entry_varchar = Entry(varchar, font='Ubuntu', width=6, justify='center')
            entry_varchar.place(x=125, y=65)
            bt_varchar = Button(varchar, text='Salvar', font='Times')
            bt_varchar.place(x=129, y=100)

        super(BancoDeDados, self).bt_create_columns()

    def connector(self):
        '''
        -> Método responsável por fazer a conexão ao banco de dados MySQL
        '''
        self.con = connector.connect(user=self.user, host=self.host, password=self.password, database=self.database)

    def exception_error(self):
        '''
        -> Método responsável por informar que houve um erro (caso haja) ao usuário e atribui ao botão opção de fechar
         o sistema.
        '''
        self.label_name['text'] = 'Houve uma falha ao conectar ao banco de dados! Consulte o .log para mais ' \
                                  'informações ou contacte o desenvolvedor!'
        self.bt_connect['command'] = lambda: self.window.destroy()
        self.bt_connect['text'] = 'Sair'
        self.bt_connect['width'] = '10'
        self.name_entry.destroy()


class BancoDeDados(Interface):
    '''
    -> Classe reponsável por construir a interface com o usuario e também herda os métodos da classe Interface.
    '''

    # Criação e configuração da interface.

    def __init__(self):
        self.window = Tk()
        self.window.geometry('1000x600+200+50')
        self.window.resizable(False, False)
        self.window.title('Consultoria de Dados MySQL - SAM')
        self.window.wm_iconbitmap('.\images\icon.ico')
        self.img = PhotoImage(file='.\images\\background.png')
        self.background_img = Label(self.window, image=self.img, background='grey11')
        self.background_img.place(x=0, y=0, relwidth=1.0, relheight=1.1)
        self.font_title = font.Font(family='Times', size=25)
        self.font_text = font.Font(family='Times', size=15)
        Label(self.window, height=50, width=5, background='grey11').pack(side='left', anchor='s')

        self.label_welcome = Label(self.window, background='grey11', fg='white', font=self.font_title, height=6,
                                   text='BEM VINDO AO CONSULTOR DE DADOS MYSQL')
        self.label_welcome.pack(side='top')

        self.label_name = Label(self.window, background='grey11', fg='white', font=self.font_text,
                                text='Digite abaixo o HOST do banco de dados que deseja conectar', height=3)
        self.label_name.pack(side='top', anchor='n')

        self.name_entry = Entry(self.window, width=30, font='Times', justify='center')
        self.name_entry.pack(side='top')

        Label(self.window, height=2, background='grey11', fg='white',).pack(side='top')

        self.bt_connect = Button(self.window, text='Confirmar', font='Times', fg='grey11',
                                 command=super(BancoDeDados, self).bt_host)
        self.bt_connect.pack(side='top')

        self.credits = Label(self.window, background='grey11', fg='white', text='developed by Samuel Nunes')
        self.credits.pack(side='bottom', anchor='se')
        self.window.mainloop()


# Criando o diretório para os logs.

dir_log = f'{Path.home()}\\Documents\\Logs'

try:
    makedirs(dir_log)
except FileExistsError:
    print('Arquivo já existente!')
except Exception as e:
    raise e

# Configurações implementadas para os arquivos .log

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
basicConfig(filename=f'{dir_log}\\{date.today()}.log', level=DEBUG, filemode='at', format=format)
logger = getLogger(__name__)
logger.info('Inicialização completa com sucesso!')

#Inicialização da interface.

interface = BancoDeDados()
