from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
#from PyQt5.QtWidgets import QApplication,QMessageBox
from datetime import datetime
class Database():
    '''
    数据库操作，包含查询密码，用户信息，和修改table，默认数据库为Sqlite
    数据库名为test.db,包含两个表 user_info(用户信息）和sign_record（考勤记录）
    不提供新建功能，只可清除表的内容
    '''

    def __init__(self):
        '''
        数据库初始化，数据库类型为Sqlite
        '''
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('test.db')
        self.database.open()
        self.query = QSqlQuery()

    def get_passwd(self,id):
        '''
        获取用户密码
        :param id: 用户名ID  type :int
        :return: 用户密码
        :type : str
        '''
        if self.query.exec('select passwd from user_info where id = %d'%id):
            while self.query.next():
                passwd = self.query.value(0)
                return passwd

    def get_user_info(self,id):
        '''
        获取用户信息
        :param id: 用户ID   type : int
        :return: 用户所有信息
        :type : dict
        '''
        if self.query.exec('select * from user_info where id = %d' % id):
            while self.query.next():
                ID = self.query.value(self.query.record().indexOf('id'))
                username = self.query.value(self.query.record().indexOf('name'))
                age = self.query.value(self.query.record().indexOf('age'))
                sex = self.query.value(self.query.record().indexOf('sex'))
                address = self.query.value(self.query.record().indexOf('address'))
                tel = self.query.value(self.query.record().indexOf('tel'))
                job = self.query.value(self.query.record().indexOf('job'))
                finger_id = self.query.value(self.query.record().indexOf('finger_id'))
                info = {'id':ID,'name':username,'age':age,'sex':sex,'address':address,'tel':tel,'job':job,'finger_id':finger_id}
                return info
                
    def change_user_info(self, new_info):
        '''
        更新用户信息
        :param info:新的用户信息 type : dict
        :return: None
        '''
        self.query.prepare('update user_info set name = ?, age = ?, job = ?, tel = ?, sex = ?, address = ? where id = %d'%(new_info['id']))
        self.query.addBindValue(new_info['name'])
        self.query.addBindValue(new_info['age'])
        self.query.addBindValue(new_info['job'])
        self.query.addBindValue(new_info['tel'])
        self.query.addBindValue(new_info['sex'])
        self.query.addBindValue(new_info['address'])
        self.query.exec_()
    
    def get_record(self):
        '''
        获取前100条签到数据
        :return: data
        :type:dict
        '''
        data = []
        buff = dict()
        if self.query.exec('select * from sign_record limit 100 '):
            while self.query.next():
                buff['time'] = self.query.value("time")
                buff['id'] = self.query.value("id")
                buff['name'] = self.query.value("name")
                buff['operation'] = self.query.value("operation")
                buff['illegal'] = self.query.value("illegal")
                data.append(buff)
                buff = dict()
            return data
            
    def get_record_by_id(self, id):
        '''
        通过id获取当前用户签到数据最多100条
        :param id:用户id type : int
        :return: data
        :type:dict
        '''
        data = []
        buff = dict()
        if self.query.exec('select * from sign_record where id = %d limit 100' % id):
            while self.query.next():
                buff['time'] = self.query.value("time")
                buff['id'] = self.query.value("id")
                buff['name'] = self.query.value("name")
                buff['operation'] = self.query.value("operation")
                buff['illegal'] = self.query.value("illegal")
                data.append(buff)
                buff = dict()
            return data
            
            
    def new_record(self, id, operation):
        '''
        添加新的考勤记录
        :param id:用户ID type:int
        :param operation : 操作代号 type:int
        :return: None
        '''
        current_time = datetime.now().strftime("%H:%M")  #获取当前时间（时：分）
        flag = judge_time_section(current_time)
        if operation == 1:
            operation ="签到"
            if flag == 1:
                illegal = "否"
            else:
                 illegal = "是"
        else:
            operation = "离开"
            if flag == 3:
                 illegal = "否"
            else:
                 illegal = "是"
        name = self.get_user_info(id)['name'] #获取对应ID的用户名
        self.query.exec('INSERT INTO sign_record([id],[name],[operation],[illegal]) VALUES(%d,\'%s\',\'%s\',\'%s\'); ' %(id,name,operation,illegal))
        
def judge_time_section(now, start = '08:30', end = '17:30'):
    '''
    判断当前时间区间
    :param now:当前时间 type:str
    :param start:开始时间 type:str
    :param end:结束时间 type:str
    :return: 标志位 type: int 
        1：小于开始时间
        2：处于开始和结束之间
        3：大于结束时间
    '''
    if now < start :
        return 1
    elif now > start and now < end:
        return 2
    elif now > end:
        return 3
    
        
