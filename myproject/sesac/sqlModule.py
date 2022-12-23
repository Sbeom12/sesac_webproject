import pandas as pd
import pymysql
from pymysql import cursors, connect 
import json
from datetime import datetime


class DBUpdater():
    
    # Database 연결
    def __init__(self):
        self.conn = pymysql.connect(
            user='root', 
            passwd='1111', 
            host='127.0.0.1', 
            db='community', 
            charset='utf8',
            # cursorclass=cursors.DictCursor
            )
        
        self.tableList = ['UserInfo', 'Board', 'Post', 'Comment']
        self.cursor = self.conn.cursor()
        self.createTable()
        
    
    # Database 연결 해제
    def __del__(self):
        
        self.conn.close()
        
    # PK 연결 & 연결 해제
    def pkConnect(self, connect):
        
        if (connect=="disconnect"):
            sql = """SET foreign_key_checks = 0;"""
            self.cursor.execute(sql)
            print("\n외래키 연결이 해제되었습니다.\n")
            
        elif (connect=="connect"):
            sql = """SET foreign_key_checks = 1;"""
            self.cursor.execute(sql)
            print("\n외래키 연결이 설정되었습니다.\n")
            
        else:
            print("\nconnect error\n")
    
    

    
    
    
    ###########################################  Create & Delete Date function  ###############################################
    # Table 생성
    def createTable(self):
        
        # userInfo
        sql = """
                CREATE TABLE IF NOT EXISTS UserInfo (
                
                userId  VARCHAR(255),
                userPw  VARCHAR(255)    NOT NULL,
                userNm  VARCHAR(255)    NOT NULL,
                subNm   VARCHAR(255)    NOT NULL    UNIQUE,
                tel     VARCHAR(255)    NOT NULL    UNIQUE,
                email   VARCHAR(255)    NOT NULL    UNIQUE,
                grade   INT             NOT NULL    DEFAULT 1,
                
                PRIMARY KEY(userId)
                )
            """
        self.cursor.execute(sql)
        
        # * Board
        sql = """
                CREATE TABLE IF NOT EXISTS Board (
                    
                brdId	   INT                     AUTO_INCREMENT,
                brdNm	   VARCHAR(255) NOT NULL   UNIQUE,
                pstNum     INT,
                
                PRIMARY KEY(brdId)
                )
            """
        self.cursor.execute(sql)
        
        # * Post
        sql = """
                CREATE TABLE IF NOT EXISTS Post (
                    
                pstId	     INT                      AUTO_INCREMENT,
                brdId        INT           NOT NULL,
                userId       VARCHAR(255)  NOT NULL,
                title        VARCHAR(255)  NOT NULL,
                pstCntnt     VARCHAR(255)  NOT NULL,
                
                pstCrtDate   TIMESTAMP                DEFAULT CURRENT_TIMESTAMP,
                finalDate    TIMESTAMP                DEFAULT CURRENT_TIMESTAMP,
                vwCnt        INT                      DEFAULT 1,
                pstLikeCnt   INT                      DEFAULT 1,
                pstUnlikeCnt INT                      DEFAULT 1,
                
                PRIMARY KEY(pstId),
                
                FOREIGN KEY (brdId) REFERENCES Board (brdId) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (userId) REFERENCES UserInfo (userId) ON UPDATE CASCADE ON DELETE CASCADE
                )
            """
        self.cursor.execute(sql)
        
        # * Comment
        sql = """
                CREATE TABLE IF NOT EXISTS Comment (

                cmtId	     INT                     AUTO_INCREMENT,
                pstId        INT          NOT NULL,
                userId       VARCHAR(255) NOT NULL,
                cmtCntnt     VARCHAR(255) NOT NULL,
                cmtCrtDate   TIMESTAMP    NOT NULL   DEFAULT CURRENT_TIMESTAMP,
                
                cmtLikeCnt   INT                     DEFAULT 1,
                cmtUnlikeCnt INT                     DEFAULT 1,

                PRIMARY KEY(cmtId),
                
                FOREIGN KEY (brdId) REFERENCES Board (brdId) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (pstId) REFERENCES Post (pstId) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (userId) REFERENCES UserInfo (userId) ON UPDATE CASCADE ON DELETE CASCADE
                )
            """
        self.cursor.execute(sql)
        self.conn.commit()
        
        
    # Table 삭제
    def deleteTable(self, table=None):
        
        self.pkConnect("disconnect")
        # 모두 삭제
        if(table==None):
            for table in self.tableList:
                sql = f"DROP TABLE {table}"
                self.cursor.execute(sql)
            print("\nTable이 모두 삭제되었습니다.\n".format(table))
            
        # 지정 table 삭제   
        else:
            sql = f"DROP TABLE {table}"
            self.cursor.execute(sql)
            print("\nTable '{}' 이(가) 삭제되었습니다.\n".format(table))
        self.pkConnect("connect")
            
            
    # Table 초기화
    def resetTable(self, table=None):
        
        self.pkConnect("disconnect")
        # 모두 초기화
        if(table==None):
            for table in self.tableList:
                sql = f"TRUNCATE TABLE {table}"
                self.cursor.execute(sql)
            print("\nTable이 모두 초기화되었습니다.\n".format(table))
        
        # 지정 table 초기화
        else:
            sql = f"TRUNCATE TABLE {table}"
            self.cursor.execute(sql)
            print("\nTable '{}' 이(가) 초기화되었습니다.\n".format(table))
        self.pkConnect("connect")
    
    ###################################################  Extract Table  #####################################################

    ############# Board ###########
    def load_board_list(self):
        sql = 'SELECT * FROM Board;'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data




    ############# Post ###########
    def load_post_list(self):
        sql = 'SELECT * FROM Post ORDER BY pstCrtDate DESC ;'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    
    def load_post_brdId_list(self, brdId):
        sql = f'SELECT * FROM Post WHERE brdId={brdId} ORDER BY pstCrtDate DESC ;'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    def load_post_pstId_list(self, pstid):
        sql = f'SELECT * FROM Post WHERE pstId={pstid};'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    def load_post_userId_list(self, userId):
        sql = f'SELECT * FROM Post WHERE userId={userId};'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    
    def update_post(self, form, pstId):
        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        brdId = form['brdId']
        title = form['title']
        pstCntnt = form['pstCntnt']
        sql = f"""
        UPDATE Post
        SET brdId = {brdId}, title=\'{title}\' , pstCntnt=\'{pstCntnt}\' ,finalDate={date} 
        WHERE pstId = {pstId};"""
        # print(sql)
        try:
            date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            brdId = form['brdId']
            title = form['title']
            pstCntnt = form['pstCntnt']
            sql = f"""
            UPDATE Post
            SET brdId = {brdId}, title=\'{title}\' , pstCntnt=\'{pstCntnt}\' ,finalDate=\'{date}\' 
            WHERE pstId = {pstId};"""
            self.cursor.execute(sql)
            self.conn.commit()
            print('update_post - success')
        except:
            print('update_post - error')
            
    def del_post(self, pstId):
        try:
            sql = f"DELETE FROM Post WHERE pstId={pstId};"
            self.cursor.execute(sql)
            self.conn.commit()
            print('del_post - success')
        except:
            print('del_post - error')
                
        
            
    def insert_comment(self, pstId , userId, cmtCntnt):
        try:
            sql = f"""
            INSERT INTO Comment  (pstId , userId, cmtCntnt)
            VALUES ({pstId},{userId},\'{cmtCntnt}\');"""
            self.cursor.execute(sql)
            self.conn.commit()
            print('insert_comment - success')
        except:
            print('insert_comment - error')
    
    def load_comm_pstId_list(self, pstId):
        sql = f'SELECT * FROM Comment WHERE pstId={pstId};'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    def load_comm_userId_list(self, userId):
        sql = f'SELECT * FROM Comment WHERE userId={userId};'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    
    def match_cmtId(self, cmtId):
        sql = f'SELECT * FROM Comment WHERE cmtId={cmtId};'
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def del_comm(self, cmtId):
        try:
            sql = f"DELETE FROM Comment WHERE cmtId={cmtId};"
            self.cursor.execute(sql)
            self.conn.commit()
            print('del_comm - success')
        except:
            print('del_comm - error')
        
    


    # Table 출력1 (Pandas DataFrame)
    def exetractDF(self, table):
    
        sql = f"SELECT * FROM {table}"
        df = pd.read_sql(sql, self.conn)
        print("\nTable '{}' 이(가) DataFrame 형태로 출력되었습니다.\n".format(table))
        return df
    
    # Table 출력2 (Json)
    def exetractJson(self, table, field=None):
        
        if(field==None):
            sql = f"SELECT * FROM {table}"
        else:
            sql = f"SELECT {field} FROM {table}"
            
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("\nTable '{}' 이(가) Json 형태로 출력되었습니다.\n".format(table))
        return data
    
    # Table 출력 3 (List)
    def exetractLi(self, table, field):
        
        sql = f"SELECT {field} FROM {table}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        
        li=[]
        for d in data:
            d = list(d)
            li.append(d[0])
        print("\nTable '{}'의 Field '{}'이(가) List 형태로 출력되었습니다.\n".format(table, field))
    
    ##################################################  Insert Date  ##################################################
    
    # rule
     # 각 table의 id들은 ai이기 때문에 직접 입력하지 않음
     # 
    
    # userInfo
     # 사용자의 type('admin', 'user')과 정보를 입력하면 저장
     # Grade에 따라 분류_ 관리자('admin'):0, 이용자('user'):1
    def insertUserInfo(self, userId, userPw, userNm, subNm ,tel, email, type="user"):
        try:
            if(type=='admin'):
                sql = f"INSERT INTO UserInfo (userId, userPw, userNm ,subNm, tel, email, grade) VALUES (\"{userId}\", \"{userPw}\", \"{userNm}\", \"{subNm}\", \"{tel}\", \"{email}\", 0)"
                self.cursor.execute(sql)
                print("\n관리자의 정보가 저장되었습니다.\n")
                
            elif(type=='user'):
                sql = f"INSERT INTO UserInfo (userId, userPw, userNm ,subNm, tel, email, grade) VALUES (\"{userId}\", \"{userPw}\", \"{userNm}\", \"{subNm}\", \"{tel}\", \"{email}\", 1)"
                self.cursor.execute(sql)
                print("\n이용자의 정보가 저장되었습니다.\n")
                
            else:
                print("\n사용자의 TYPE을 정확하게 입력해주세요.\n")
            self.conn.commit()    
            
        except:
            print("\n정보가 없거나, 이미 등록된 정보입니다.\n")
    
    # Board 
    def insertBoard(self, brdNm, pstNum):
        try:
            sql = f"INSERT INTO Board (brdNm, pstNum) VALUES (\"{brdNm}\", {pstNum})"
            self.cursor.execute(sql)
            self.conn.commit()
            print("\n게시판이 생성되었습니다.\n")
        except:
            print("\n내용이 없거나, 이미 등록된 게시판입니다.\n")
  
    # Post (linked Board)
    def insertPost(self, brdId, userId, title, pstCntnt):
        try:
            sql = f"INSERT INTO Post (brdId, userId, title, pstCntnt) VALUES ({brdId}, \"{userId}\", \"{title}\", \"{pstCntnt}\")"
            self.cursor.execute(sql)
            self.conn.commit()
            print("\n게시물이 저장되었습니다.\n")
        except:
            print("\n이미 등록되어 있는 게시물이거나, 유효하지 않은 PK 입니다.\n")
        
        '''
        pstId, brdId, userId, title, pstCntnt
        pstCrtDate, finalDate, vwCnt, pstLikeCnt, pstUnlikeCnt
        '''
        
    # Comment (linked Board, Post)
    def insertComment(self, brdId, pstId, userId, cmtCntnt):
        try:
            sql = f"INSERT INTO Comment (brdId, pstId, userId, cmtCntnt) VALUES ({brdId}, {pstId}, \"{userId}\", \"{cmtCntnt}\")"
            self.cursor.execute(sql)
            self.conn.commit()
            print("\n댓글이 저장되었습니다.\n")
        except:
            print("\n이미 등록되어 있는 댓글이거나, 유효하지 않은 PK 입니다.\n")
        
        '''
        cmtId, brdId, pstId, userId, cmtCntnt, cmtCrtDate
        cmtLikeCnt, cmtUnlikeCnt
        '''


    ################################################  Extract Date  ###############################################

    # 조건에 맞는 값 출력하는 함수
    # 순서대로 출력할 데이터의 'field', 원하는 table, 조건 condition, 조건의 값 value
    def extractWhere(self, field, table, conditon, value):
        try:
            sql = f"SELECT {field} FROM {table} WHERE {conditon} = \"{value}\""
            self.cursor.execute(sql)
            data = self.cursor.fetchall()[0][0]
            print("\n존재하는 {}입니다.\n입력한 {}의 {}이(가) 출력되었습니다.\n".format(conditon, conditon, field))
            return data
        except:
            print("\n존재하지 않는 {}입니다.\n".format(conditon))


    ################################################  Modify Date  ################################################
    
    # userInfo
    # Board
    # Post
    # comment
    

    
    
    
    ################################################  Delete Date  ################################################
    
    # user가 삭제하고 linked 된 post, comment 삭제
    def deleteUserInfo(self, userId):
        sql = f"DELETE FROM userInfo where userId= \"{userId}\""
        self.cursor.execute(sql)
        self.conn.commit()
        print("\nuserId '{}'가 삭제되었습니다.\n".format(userId))
     
    # board가 삭제하고 linked 된 post, comment 삭제
    def deleteBoard(self, brdId):
        sql = f"DELETE FROM Board where brdId={brdId}"
        self.cursor.execute(sql)
        self.conn.commit()
        
    # post가 삭제하고 linked 된 comment 삭제
    def deletePost(self, pstId):
        try:
            sql = f"DELETE FROM Post where pstId={pstId}"
            self.cursor.execute(sql)
            self.conn.commit()
            print("\n게시물이 삭제되었습니다.\n")
        except:
            print("\n등록되어 있지 않은 게시물입니다.\n")
    
    # comment 삭제
    def deleteComment(self, cmtId):
        try:
            sql = f"DELETE FROM Comment where cmtId={cmtId}"
            self.cursor.execute(sql)
            self.conn.commit()
            print("\n댓글이 삭제되었습니다.\n")
        except:
            print("\n등록되어 있지 않은 댓글입니다.\n") # 이게 왜 안돼: 외래키 해제 시켜놔서 바보야
    
    ########################################################################################################
        
if __name__ == "__main__":
    print("\n실행 완료\n")
    x = DBUpdater()
    x.__del__
