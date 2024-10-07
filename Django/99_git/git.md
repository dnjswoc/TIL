# 2024년 10월 4일(금) - git 내용 정리

### git

```bash
# 이 폴더를 git으로 관리하겠다.
$ git init
```

- 현재 작업중인 폴더 내의 .git을 제외한 폴더 위치를 `working directory`

- working directory 에만 작성한 내용은 아직은 git이 어떤 변동사항이 있는지 모른다.

```bash
# staging area에 해당하는 파일을 등록
$ git add {fili_path}
```

- `staging area` 란, 등록한 파일들의 변도사항만 기록한 txt 파일을 `.git` 폴더 어딘가에 모아둔다.


```bash
# staging area에 등록해둔 변동사항을
# 하나의 버전으로 기록한다.
# 그 후, staing area는 비운다.
$ git commit -m "commit message"
```
- git add, git commit 까지가 Local에서 작업

- `commit` 즉, 버전이란, 아까 전 `staging area`에 등록해둔, 변동사항만을 모아서 하나의 상태로 저장하낟.
- 그곳을 `repository` 라고 부른다.

- example.
  - 신발 밑창을 단상에 올리는게 add.....
  - 밑창 사진을 찍어 올리는게 commit...(하나의 version?)


- remote repository...(github, gitlab 등)
  - 원격 레포지토리에 올리려면 push...?

<br>

```bash
$ git push origin master
# origin : 원격 저장소의 별명
# master : branch의 개념
```




### branch


```bash
# 브랜치 목록 확인
$ git branch
# 브랜치 생성
# 브랜치 생성한 작업영역의 최신버전을 따라서 만들어진다.
$ git branch {branch_name}
# 브랜치 삭제(대문자 D XXX)
$ git branch -d {branch_name}
# Merge()
$ git merge {branch_name}
# Merge 그래프 확인(first commit : root node)
$ git log --oneline --graph
```


#### git branch

- 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구


#### branch 장점

1. 독립된 개발 환경을 형성하기 때문에 원본(master)에 대해 안전
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능
3. 손쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있음


#### branch를 꼭 사용해야 할까?

- 만약 상용 중인 서비스에 발생한 에러를 해결하려면?
  1. 브랜치를 통해 별도의 작업 공간을 만든다.
  2. 브랜치에서 에러가 발생한 버전을 이전 버전으로 되돌리거나 삭제한다.
  3. 브랜치는 완전하게 도립 되어있어서 작업 내용이 master 브랜치에 아무런 영향을 끼치지 못한다.
  4. 이후 에러가 해결됐다면? 그 내용을 master 브랜치에 반영할 수 있다.


#### git branch

- 브랜치 조회, 생성, 삭제 등 브랜치와 관련된 git 명령어

|명령어|기능|
|:---|:---|
|git branch|브랜치 목록 확인|
|git branch -r|원격 저장소의 브랜치 목록 확인|
|git branch <브랜치 이름>|새로운 브랜치 생성|
|git branch -d <브랜치 이름>|브랜치 삭제(병합된 브랜치만 삭제 가능)|
|git branch -D <브랜치 이름>|브랜치 삭제(강제 삭제)|
<br>

#### git switch

|명령어|기능|
|:---|:---|
|git switch <다른 브랜치 이름>|브랜치 목록 확인|
|git switch -c <브랜치 이름>|원격 저장소의 브랜치 목록 확인|
|git switch -c <브랜치 이름> <commit ID>|새로운 브랜치 생성|
<br>

#### Merge

1. 새로 만든 브랜치가 원본으로 바라보고 있던 작업영역에서 혼자 commit을 하고, 원본에는 변동이 없을 때 FF(Fast Foward, 빨리감기) merge
  - 이때는 commit message를 만들 필요가 없다.

2. 원본도 변동이 있고, 새로 만든 브랜치도 원본이 있을 때는 3 way merge
  - 새로운 버전을 만들어야 하므로 commit을 해야하고 commit message를 작성한다.


```bash
# 원격과 local의 차이점 확인 가능
$ git fetch origin master
```