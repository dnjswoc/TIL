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
        - (./이미지 파일명)을 통해서 다운로드 받은 이미지를 삽입할 수 있다.
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


# 7월 12일 수업 내용 정리
## Remote Repository

- 원격 저장소(Remote Repository) : 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간(GitLab, GitHub, Bitbucket 등)
- 로컬&원격 저장소
    - 로컬 저장소와 원격 저장소 둘의 관계는 remote

### Remote Repository 사용법
- git remote add origin(추가하는 원격 저장소 별칭, 관행) remote_repo_url : 로컬 저장소 한 개에 여러 원격 저장소 추가
- git remote -v : 원격 저장소 위치 확인(fetch, push, git pull = git fetch + git merge)
- push : 로컬에서 원격으로
- git push origin master : origin이라는 이름의 원격 저장소에 master라는 브랜치로 commit 목록 업로드
- 터미널 메시지를 통해 push가 성공했다는 것을 확인
- 원격 저장소에 commit 목록이 잘 push되었는지 확인
- 로컬 저장소에 commit 생성
- 로컬 head, 원격 head가 같은 commit에 있으면 최신 정보가 동기화 된 것이다.
- Github의 repository에서 commits을 누르고 view commit details : 원격 저장소의 commit 정보를 자세하게 확인 가능
- 원격 저장소에는 commit이 올라가는 것(commit 이력이 없다면 push할 수 없다.)
- pull & clone : 원격 저장소에서 로컬 저장소로 옮기기
- git pull origin master : 원격 저장소의 변경사항만을 받아옴(업데이트)
- git clone remote_repo_url : 원격 저장소 전체를 복제(다운로드, clone으로 받은 프로젝트는 이미 git init이 되어 있음, .git 폴더가 중복될 수 있음을 주의)
- mv -f first-repo git_advanced : 폴더 이름 바꾸기(CLI에서)
- repository에서 setting - collaborators를 통해 같이 해당 repository를 작업할 동료를 지정할 수 있다.

## Git revert & reset
- gitignore : Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정
- .gitignore 파일 생성(git init 이전에 생성해야 한다)
- a.txt, b.txt 파일 생성
- gitignore에 a.txt 작성
- git init
- git status
- 이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 
- gitignore 목록 생성 서비스 : 운영체제, 프레임워크, 프로그래밍 언어 등 개발 환경에 따라 gitignore 목록을 만들어주는 [사이트](https://www.toptal.com/developers/gitignore/)

### GitHub 활용하기
- TIL을 통해 내가 학습하는 것을 기록
- 개인, 팀 프로젝트 코드를 공유
    - 개발 면접 지원 시 본인의 GitHub주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
- 오픈 소스 프로젝트에 기여
#### TIL(Today I Learned)
- 매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것
- 단순히 배운 것만을 필기하는 것이 아닌 스스로 더 나아가 어떤 학습을 했는지를 기록하는 것

- 문서화의 중요성 : 신입 개발자에게 요구되는 가장 중요한 덕목 [링크](https://d2.naver.com/news/3435170)
- TIL 만들기
    - TIL이라는 이름의 GitHub Repository 생성
    - 로컬 저장소 설정
    - REAMME.md 생성 및 지금까지의 수업 내용을 정리하고 commit을 생성
    - TIL 원격 저장소를 추가
    - commit 목록을 push
- READMD.md 파일이란?
    - 프로젝트에 대한 설명, 사용 방법, 문서화된 정보 등을 포함하는 역할
    - Markdown 형식으로 작성되며, 프로젝트의 사용자, 개발자, 혹은 기여자들에게 프로젝트에 대한 전반적인 이해

## [부록] Git Undoing
