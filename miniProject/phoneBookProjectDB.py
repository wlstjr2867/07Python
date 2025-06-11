import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8', port=3306)
curs = conn.cursor()

def menu():
  print('원하시는 메뉴를 입력하세요')
  print('1. 입력 2.출력 3.검색 4.수정 5.삭제 6.종료' )
  return input('번호선택:')

def insert_data():
  print(f"{'입력기능':-^30}")
  name = input("이름:")
  phone = input("전화번호:")
  address = input("주소:")
  
  sql = "INSERT INTO phonebooks (name, phone, address) VALUES(%s, %s, %s)"
  try:
    curs.execute(sql, (name, phone, address))
    conn.commit()
    print("1개의 레코드가 입력됨")
  except Exception as e :
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
  
def output_data():
  print(f"{'출력기능':-^30}")
  sql = "SELECT * FROM phonebooks"
  try:
    curs.execute(sql)
    rows = curs.fetchall()
    
    if not rows:
      print("등록된 데이터가 없습니다.")
      
    for row in rows:
      print(f"[{row[0]}]")
      print(f"이름: {row[1]}")
      print(f"전화번호: {row[2]} ")
      print(f"주소: {row[3]}")
      print()
  except Exception as e :
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
    
def search_data():
  print(f"{'검색기능':-^30}")
  search_name = input("검색할 이름을 입력하세요: ")
  
  sql = "SELECT * FROM phonebooks WHERE name = %s"
  try:
    curs.execute(sql, (search_name,))
    rows = curs.fetchall()
    
    if not rows:
      print("검색 결과가 없습니다.")
      return
    
    for row in rows:
      print(f"[{row[0]}]")
      print(f"이름: {row[1]}")
      print(f"전화번호: {row[2]} ")
      print(f"주소: {row[3]}")
      print()
  except Exception as e :
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
    
def edit_data():
  print(f"{'수정기능':-^30}")
  edit_name = input("수정할 이름을 입력하세요: ")
  
  sql_select = "SELECT idx, name, phone, address FROM phonebooks WHERE name = %s"
  try:
    curs.execute(sql_select, (edit_name,))
    rows = curs.fetchall()
    
    if not rows:
      print("찾을 수 없습니다.")
      return
    
    row = rows[0]
    
    print(f"현재 이름: {row[1]}")
    new_name = input("새 이름 입력하세요 (변경하지 않으려면 Enter): ")
    if new_name.strip() == "":
      new_name = row[1]
    
    print(f"현재 전화번호: {row[2]}")
    new_phone = input("새 전화번호를 입력하세요 (변경하지 않으려면 Enter): ")
    if new_phone.strip() == "": 
      new_phone = row[2]
    
    print(f"현재 주소: {row[3]}")
    new_address = input("새 주소를 입력하세요(변경하지 않으려면 Enter): ")
    if new_address.strip() == "":
      new_address = row[3]
      
    sql_update = """
      UPDATE phonebooks
      SET name = %s, phone = %s, address = %s
      WHERE idx = %s """
    curs.execute(sql_update, (new_name, new_phone, new_address, row[0]))
    conn.commit()
    print("정보가 수정되었습니다")
  except Exception as e:
    conn.rollback()
    print("수정 중 오류 발생:", e)
        
def delete_data():
  print(f"{'삭제기능':-^30}")
  delete_name = input("삭제할 이름을 입력하세요:")
  
  sql_select = "SELECT idx, name, phone, address FROM phonebooks WHERE name = %s"
  try:
    curs.execute(sql_select, (delete_name,))
    rows = curs.fetchall()
    
    if not rows:
      print("해당 이름의 정보를 찾을 수 없습니다.")
      return
    
    row = rows[0]
    
    sql_delete = "DELETE FROM phonebooks WHERE idx = %s"
    curs.execute(sql_delete, (row[0],))
    conn.commit()
    print("정보가 삭제되었습니다.")
    
  except Exception as e :
    conn.rollback()
    print("쿼리 실행시 오류발생", e)


choice = 0

while True:
  choice = int(menu())
  if choice == 1:
    insert_data()
  elif choice == 2:
    output_data()
  elif choice == 3:
    search_data()
  elif choice == 4:
    edit_data()
  elif choice == 5:
    delete_data()
  elif choice == 6:
    print("프로그램종료")
    conn.close()
    break