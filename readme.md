# 7월 11일 수업 내용 정리
## Markdodwn
### Markdown(개발자의 언어)의 특징
- 쓰면서 서식을 지정
- 코드를 옮기기 쉽다.
- 배우기 쉽다.


### 1. Markdown 문법
1. Heading
    - #(샵) 개수에 따라 제목 서식 지정 가능(최대 6개)
2. List
    - 숫자를 지정하면 순서가 있는 목록을 만들 수 있고, 숫자를 지정하지 않으면 순서가 없는 목록을 만들 수 있다.
    - tab을 통해서 목록 순위를 추가할 수있다.
    - shift + tab을 통해 목록 순위를 낮출 수 있다.
3. Code block & Inline code block
    - 개발에서 마크다운을 사용하는 가장 큰 이유
    - `(백틱)을 통해 표현 가능
    - ex.
    ```python
    print('hello')
    print('world')
    ```
    - 본문 중에 코드를 삽입하고 싶을 때는 백틱 하나를 다음과 같이 `print`사용하면 된다.
4. 링크 & 이미지
    - 대괄호와 소괄호를 사용하여 링크 삽입 가능
    - 이미지는 링크 사용하는 방법 앞에 !만 추가하면 된다.
    - ex. [구글](https://www.google.com)
    - ex.
    ![mountain](https://picsum.photos/200/300)
5. 텍스트
    - 굵게 : **사용, ex. **굵게**
    - 기울임 : *사용, ex. *기울임*
    - 취소선 : ~~사용, ex. ~~취소선~~
    - 수평선 : ---(hypen) 3개 이상 적으면 적용
    ---
- 그 외에도 마크다운 문법은 마크다운 가이드를 통해 자세히 알 수 있다.
- 마크다운 작성을 도와주는 마크다운 에디터
    - [Typora](https://typora.io/)(유료)
    - [MarkText](https://www.marktext.cc/)(무료)
    - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)(VSCode 확장프로그램)


## 2. CLI(Command Line Interface)
### CLI란?
- 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식, CLI는 키보드만으로 모든 작업을 수행할 수 있다.
### GUI란?
- 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
### CLI문법
1. cd : 디렉토리 변경, cd ..을 사용하면 상위 디렉토리로 변경할 수 있다.
2. mkdir : 새 디렉토리 생성
3. ls : 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
4. ls -a : 숨긴 파일 모두 보기
5. touch : 파일 생성
6. start : 폴더/파일 열기
7. rm : 파일 삭제(디렉토리 삭제는 -r 옵션을 추가 사용)
8. code . : VSCode로 열기
9. pwd(print walking directory) : root 디렉토리부터 목적 지점까지 거치는 경로를 전부 작성한 것

- **CLI에서 가장 중요한 것은 내가 어디 있는지 알아야 하는 것이다.**


## 3. Git : 분산 버전 관리 시스템
- 버전 관리 : 변화를 기록하고 추적하는 것
- 분산식으로 여러 개의 복제된 저장소에 저장 및 관리하며, 변경 이력과 코드를 로컬 저장소에 기록하고, 중앙 서버에 동기화

### Git의 3가지 영역
- Working directory : 실제 작업 중인 파일들이 위치하는 공간(Untracked, Modified)
- Staging area : Working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역, 임시적 공간(New file, Modified)
- Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨(Nothing to commit, Working tree clean)

### Git의 문법
1. git init : 로컬 저장소 설정, git의 버전 관리를 시작할 디렉토리에서 진행
2. git add : 변경사항이 있는 파일을 staging area에 추가
3. git commit : staging area에 있는 파일들을 저장소에 기록, 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
    - commit을 작성하기 위해서는 commit 작성자 정보가 필요
    - git config --global user.email "이메일주소"
    - git config --global user.name "이름"
    - git config --global -l : git global 설정 정보 보기
4. git status : 로컬 저장소의 파일 상태 확인
5. git rm --cached (file) : staging area에서 제거
6. git log : commit 목록 확인, repositoty 히스토리 보기, 가장 최근의 commit이 제일 위에 올라와있다.
    - git log --oneline : commit 해시번호와 commit 이름만 간단하게 출력
7. git restore --staged (file) : 다시 working directory에 내려보내기
8. git commit --amend : VIM 편집 모드에 들어간 후 I로 insert로 바꾼 후 수정, 수정 후 esc 누르고(커맨드 모드) :wq 입력하면 수정 완료
    - 불필요한 commit을 생성하지 않고, 직전 commit을 수정할 수 있기 때문에 git에서 꼭 필요한 기능 중 하나라고 볼 수 있다.

### Git 예시
- git init
- git status
- git rm --cached sample.txt
- git add sample.txt
- git config --global user.email "dnjswoc@gmail.com"
- git config --global user.name "dnjswoc"
- git commit -m 'first commit'
- git log
- git log --oneline
- git commit --amend -> i로 편집 모드 변경 -> 수정 -> esc로 커맨드 모드 변경 -> :wq로 종료 -> 변경 완료
