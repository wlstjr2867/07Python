/*
블럭단위 주석은 Java와 동일하게 작성
*/

# 라인단위 주석은 #입니다

/*
실행방법
F9 : 현재 문서의 전체 쿼리문을 실행한다.
Ctrl + F9 : 블럭으로 지정한 쿼리만 실행한다.
	만약 쿼리문의 절반 정도만 선택하면 에러가 발생한다.
Ctrl + Shift + F9 : 현재 쿼리를 실행한다. 단 마지막에 기술한
	세미콜론 안으로 커서를 옮긴후 실행해야 한다.
*/

/*
테이블 생성하기
제약조건
	PRIMARY KEY : 기본키 지정. null값이나 중복값을 가질 수 없는
		컬럼으로 지정됨
	AUTO_INCREMENT : 자동증가 컬럼으로 지정. 1씩 증가하는 순차적인
		정수값이 자동으로 입력됨. 오라클의 시퀀스와 유사함.
	UNSIGNED : 정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고
		양수의 범위만 사용. 이때 양의 범위가 2배로 늘어남
*/
# 1.숫자형으로 구성된 테이블
CREATE TABLE tb_int (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT ,
	
	fnum1 FLOAT(10,5) NOT NULL,
	fnum2 DOUBLE(20,10)
);
DESC tb_int;

/*
레코드 입력하기
형식1 : 일련번호 idx 컬럼은 insert문에서 생략하고 작성한다.
	자동증가 컬럼으로 지정되었으므로 순차적인 번호가 자동으로
	부여된다. 즉, 자동증가 컬럼은 insert문에서 생략하는게 기본이다.
*/
INSERT INTO tb_int (num1,num2,num3,num4,fnum1,fnum2)
VALUES (123, 12345, 1234567, 1234567890,
		  12345.12345, 1234567890.1234567890);
SELECT * FROM tb_int;

/*
형식2 : insert문 작성시 컬럼을 명시하지 않으면 전체 컬럼에 대해
	입력값을 기술해야 하므로 실행시 오류가 발생할 수 있어 권장하지
	않는다.
*/
INSERT INTO tb_int
VALUES(2, 123, 12345, 1234567, 1234567890,
		 12345.12345, 1234567890.1234567890);
SELECT * FROM tb_int;

# 2. 날짜형으로 구성된 테이블
/*
CURRENT_TIMESTAMP : 날짜형식으로 지정된 컬럼에 디폴트값으로 현재시각
	을 입력할때 사용한다.
NOW() : 날짜 형식으로 지정된 컬럼에 현재시각을 입력한다. 초단위까지의
	시간이 입력된다. 오라클의 sysdate와 동일한 역할을 한다. 
*/
CREATE TABLE tb_date(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT CURRENT_TIMESTAMP
);
DESC tb_date;

INSERT INTO tb_date (DATE1, DATE2) VALUES('2023-02-25', NOW());
INSERT INTO tb_date (DATE1) VALUES('2023-02-27');
SELECT * FROM tb_date;

# 3.문자형
CREATE TABLE tb_string(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 TEXT
);
DESC tb_stringsample_db;

INSERT INTO tb_string (str1, str2) values('난 짧은글3', '난 엄청 긴글3');
SELECT * FROM tb_string;

# 4.특수형
/*
enum : 여러 항목 중 1개만 선택할 수 있는 타입.
 	HTML의 radio와 유사함.
set : 여러 항목 중 2개 이상을 선택할 수 있는 타입,
 	HTML의 checkbox와 유사함
*/
CREATE TABLE tb_spec (
	idx INT AUTO_INCREMENT,
	
	spec1 ENUM('M','W','T'),
	spec2 SET('A','B','C','D'),
	/* 아웃라인 방식으로 컬럼을 먼저 생성한 후 별도로
	기본키를 저장함 */
	PRIMARY KEY (idsample_dbx)
);

INSERT INTO tb_spec (spec1, spec2) VALUES('W', 'A,B,C');#정상입력

INSERT INTO tb_spec (spec1, spec2) VALUES('X', 'A,B,C');#spec1에러
INSERT INTO tb_spec (spec1, spec2) VALUES('M', 'X,B,C');#spec2에러

/*
spec1 컬럼은 not null로 지정하지 않았으므로 null을 허용하는 컬럼으로
정의된다. 따라서 값을 입력하지 않아도 된다.
*/
INSERT INTO tb_spec (spec2) VALUES('B,C,D');
SELECT * FROM tb_spec;

#파이썬 실습을 위한 테이블 생성
CREATE TABLE board
(
	num INT NOT NULL AUTO_INCREMENT, /*일련번호. 자동증가컬럼.*/
	title VARCHAR(100) NOT NULL, /* 제목 : 짧은 텍스트 */
	content TEXT NOT NULL, /* 내용: 긴 텍스트 */
	id VARCHAR(30) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP, /* 작성일. 현재시각
								을 디폴트 값으로지정 */
	visitcount MEDIUMINT NOT NULL DEFAULT 0, /* 조회수 */
	PRIMARY KEY (num)
);

#더미 데이터 입력
#특히 일련번호 컬럼은 쿼리문에서 생략한 상태로 작성한다.
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목1', '내용입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목2', '내용2입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목3', '내용3입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목4', '내용4입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목5', '내용5입니다','korea',NOW(),0);

SELECT * FROM board;