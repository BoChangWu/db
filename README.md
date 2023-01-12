# DB Connection

## 介紹
由於在開發 Django 與其他 Project 合作時, 有些 Table 都會共用, 若在 Django 上定義 Model 則在 Django 上開發會很方便使用, 但若把這一部份抽離出來, 使其變成在任何 python project 都可以使用, Table 的結構較能保持一致, 相關的開發者們合作開發時也不會因為資訊不對等或不理解結構而拖延開發進度, 在合作時只需要確定 Project 中的 Table 結構一致, 也就是只要共用這一部分的檔案即可, 此外, 使用此 Project 開發基本功能方便且不像 pymysql 和 pymssql 只能對單一一種 DB 連線, 甚至在對 DB 進行欄位變更時也較方便

## 使用方法

以下提供基本使用方法, 若需要特殊的功能也可以在 Script 中自行開發

### 建立 Table

#### Step 1
請在 db_model.py 中定義 Table的結構, 範例如下:
```python
class User_Account(Base):

    __tablename__ = 'User_Account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    nickname = Column(String)
    number  = Column(String(30))
    gender = Column(Integer)

    cols = {
        'id': id,
        'name': name,
        'fullname': fullname,
        'nickname': nickname,
        'number': number,
        'gender': gender
    }

    def __repr__(self):
        return f"User(id={self.id!r},name={self.name!r}, fullname={self.fullname!r})"
``` 
其中 __tablename__ 代表你想在這個 Model在 DB 中想要的名稱, 為了方便, "建議" 與 Class 的命名保持一致如上面範例, 而Column, String, Integer 等型態 Class 是由 SQLalchemy 提供, 若有需要其他 Type 可以自行 import , 詳細內容請參考[SQL Datatype Objects](https://docs.sqlalchemy.org/en/14/core/types.html)

範例下方的 cols 中請加入上方所定義的欄位並保持名稱一致, 這是為了 db_connection.py 搜尋欄位方便

在 Script 的最後會看到如下方的 Code :
```Python
Models = {
    'User_Account' : User_Account
}
```
這也如同 cols 一樣, 是為了db_connection.py 搜尋方便而定義, 在新增 Table 時"請記得" 在此處新增, 否則 db_connection.py 會找不到你的 Model

#### Step 2
由於在查詢和新增你會一次讀取或塞入多筆完整資料, 所以在這兩個功能會需要 dict 與 Table class 之間的轉換, 為此, 須在 db_model_parser.py 中定義你 Table 的 load & parse function 如下

```python
class User_handler():
    def parse(self,data=None) -> User_Account:

        if data != None:
            return User_Account(
                name = data['name'],
                fullname = data['fullname'],
                nickname = data['nickname'],
                number  = data['number'],
                gender = data['gender']
                )

    def load(self,data: User_Account) -> dict:
        return {
            'id':data.id, 
            'name': data.name,
            'fullname': data.fullname,
            'nickname' : data.nickname,
            'number'  : data.number,
            'gender' : data.gender
            }
```
同樣地, Script 最下面會有一個為搜尋方便而定義的 dict , 請在定義玩 load & parse 後將他加入到這裡
```python
Model_Parser = {
    'User_Account': User_handler
}
```
#### Step 3
若你是剛要在 DB 中建立你的設定或只是建立一個全新的 Table , 可以使用 DB_sqlalchemy 中的 create_table_all() , 若是新增或刪除 Table 中的欄位, 請使用 db_migrate(), db_migrate() 可以給 Table 名稱下指令,例如:

```python
from db_connection import *
from setting import MSSQL

sql = DB_sqlalchemy(MSSQL)
sql.db_migrate('User_Account')
```
如此就能保持 DB 與 db_model.py 的設定一致, 請注意, 你和你的共同開發者在 db_model.py 的設定一定要保持一致, 否則還是會有資訊不對等的問題

### 查詢、新增、修改、刪除

db_connection.py 中含有些基本功能, 若需要其他功能可以在標示處自行定義, 
