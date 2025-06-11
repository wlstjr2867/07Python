data = []

def menu():
  print('원하시는 메뉴를 입력하세요')
  print('1. 입력 2.출력 3.검색 4.수정 5.삭제 6.종료' )
  return input('번호선택:')

def insert_data():
  print(f"{'입력기능':-^30}")
  name = input("이름:")
  phone = input("전화번호:")
  address = input("주소:")
  
  person = {
    "이름": name,
    "전화번호": phone,
    "주소": address
  }
  data.append(person)
  print("주소 입력 완료!")

def output_data():
  print(f"{'출력기능':-^30}")
  for idx, person in enumerate(data, start=1):
    print(f"[{idx}]")
    print(f"이름: {person['이름']}")
    print(f"전화번호: {person['전화번호']} ")
    print(f"주소: {person['주소']}")
    print()

def search_data():
  print(f"{'검색기능':-^30}")
  search_name = input("검색할 이름을 입력하세요: ")
  found = False
  
  for idx, person in enumerate(data, start=1):
    if person["이름"] == search_name:
      print(f"[{idx}]")
      print(f"이름: {person['이름']}")
      print(f"전화번호: {person['전화번호']} ")
      print(f"주소: {person['주소']}")
      print()
      found = True
    
    if not found:
      print("검색 결과가 없습니다.")

def edit_data():
  print(f"{'수정기능':-^30}")
  edit_name = input("수정할 이름을 입력하세요: ")
  for person in data:
    if person["이름"] == edit_name:
      print(f"현재 이름: {person["이름"]}")
      new_name = input("새 이름 입력하세요 (변경하지 않으려면 Enter): ")
      if new_name.strip() != "":
        person["이름"] = new_name
      
      print(f"현재 전화번호: {person["전화번호"]}")
      new_phone = input("새 전화번호를 입력하세요 (변경하지 않으려면 Enter): ")
      if new_phone.strip() != "":
        person["전화번호"] = new_phone
      
      print(f"현재 주소: {person['주소']}")
      new_address = input("새 주소를 입력하세요(변경하지 않으려면 Enter): ")
      if new_address.strip() != "":
        person["주소"] = new_address
      
      print("정보가 수정되었습니다.")
      return
  print("찾을 수 없습니다.`")
        
      
def delete_data():
  print(f"{'삭제기능':-^30}")
  delete_name = input("삭제할 이름을 입력하세요:")
  for i, person in enumerate(data):
    if person["이름"] == delete_name:
      del data[i]
      print("정보가 삭제되었습니다.")
      return
  print("해당 이름의 정보를 찾을 수 없습니다.")


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
    break 