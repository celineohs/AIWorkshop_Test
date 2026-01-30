---
name: github-update
description: 프로젝트 변경사항을 GitHub에 업데이트합니다. "GitHub 업데이트", "커밋", "푸시" 요청 시 사용합니다.
---

# GitHub 업데이트 (github-update)

## 목적

프로젝트의 변경사항을 **사용자의 GitHub 저장소**에 커밋하고 푸시합니다.

---

## ⚠️ 필수: 사용자 정보 입력받기

### AI Agent는 반드시 다음 정보를 사용자에게 물어봐야 합니다:

```
1. GitHub 사용자명 (username)
   예: "yujin-yun"

2. 저장소 이름 (repository name)
   예: "sapa-demo"
   
3. (선택) 커밋 메시지
   예: "feat: State-level analysis 추가"
```

### 질문 템플릿

```
GitHub에 업로드하기 위해 몇 가지 정보가 필요합니다:

1. GitHub 사용자명이 뭔가요? (예: yujin-yun)
2. 저장소 이름은요? (예: sapa-demo, 없으면 새로 만들어야 해요)
3. 커밋 메시지는 어떻게 할까요? (기본값: 변경사항 자동 요약)
```

---

## AI Agent 동작 순서

### Step 1: 사용자 정보 수집

**반드시 먼저 물어보기:**
- GitHub username
- Repository name
- (선택) 커밋 메시지

### Step 2: Git 저장소 확인 및 초기화

```bash
# 저장소 확인
git status

# 저장소가 없으면 초기화
git init
git branch -M main
```

### Step 3: .gitignore 생성 (없으면)

```bash
# .gitignore 파일이 없으면 생성
```

**.gitignore 내용:**
```
# Python
__pycache__/
*.py[cod]
*.pyo
.ipynb_checkpoints/

# Virtual environments
venv/
env/
.env

# IDE
.vscode/
*.code-workspace

# OS
.DS_Store
Thumbs.db

# Large data files (선택적 - 사용자에게 확인)
# data/raw/*.csv
# data/raw/*.RData
```

### Step 4: 변경사항 확인

```bash
git status
git diff --stat
```

**사용자에게 변경된 파일 목록 보여주기**

### Step 5: 스테이징 및 커밋

```bash
git add .
git commit -m "[사용자가 제공한 메시지 또는 자동 생성]"
```

### Step 6: 원격 저장소 설정

```bash
# 원격 저장소 확인
git remote -v

# 없으면 추가 (사용자 정보 사용)
git remote add origin https://github.com/[USERNAME]/[REPO_NAME].git
```

### Step 7: 푸시

```bash
git push -u origin main
```

**인증 필요 시 안내:**
```
GitHub 인증이 필요합니다.
- HTTPS: 브라우저에서 로그인 팝업이 뜰 수 있어요
- SSH: SSH 키가 설정되어 있어야 해요
```

---

## 대화 흐름 예시

```
사용자: "GitHub에 올려줘"

AI Agent: 
"GitHub에 업로드하기 위해 정보가 필요해요:

1. GitHub 사용자명이 뭔가요?
2. 저장소 이름은요? (없으면 먼저 GitHub에서 만들어주세요)
3. 커밋 메시지는요? (안 알려주시면 자동으로 작성할게요)"

사용자: "yujin-yun, sapa-personality-demo"

AI Agent:
"확인했어요!
- 사용자: yujin-yun
- 저장소: sapa-personality-demo
- URL: https://github.com/yujin-yun/sapa-personality-demo

변경된 파일을 확인할게요..."

[git status 실행]

"변경된 파일 5개:
- notebooks/04_state_analysis.ipynb
- reports/step4_state.json
- ...

이대로 커밋할까요?"

사용자: "응"

AI Agent:
[git add, commit, push 실행]

"✅ GitHub 업데이트 완료!
https://github.com/yujin-yun/sapa-personality-demo"
```

---

## 커밋 메시지 자동 생성 규칙

사용자가 메시지를 제공하지 않으면:

```python
# 변경된 파일 기반 메시지 생성
if "notebooks" in changed_files:
    prefix = "feat"
    content = "노트북 업데이트"
elif "reports" in changed_files:
    prefix = "docs"
    content = "결과 저장"
elif "skills" in changed_files:
    prefix = "chore"
    content = "스킬 업데이트"
else:
    prefix = "chore"
    content = "프로젝트 업데이트"

message = f"{prefix}: {content}"
```

| 접두사 | 조건 | 예시 |
|--------|------|------|
| `feat:` | 노트북 변경 | `feat: State analysis 추가` |
| `docs:` | reports 변경 | `docs: step4 결과 저장` |
| `chore:` | skills/기타 | `chore: github-update 스킬 추가` |

---

## 에러 처리

### 저장소가 없을 때
```
"GitHub에 저장소가 없는 것 같아요.
https://github.com/new 에서 '[REPO_NAME]' 저장소를 먼저 만들어주세요!"
```

### 인증 실패
```
"GitHub 인증에 실패했어요.
- Personal Access Token 설정: https://github.com/settings/tokens
- 또는 GitHub CLI 로그인: gh auth login"
```

### 충돌 발생
```
"원격 저장소와 충돌이 있어요.
먼저 git pull을 실행할까요?"
```

---

## 체크리스트

- [ ] 사용자에게 GitHub username 물어봤는가?
- [ ] 사용자에게 저장소 이름 물어봤는가?
- [ ] .gitignore 파일 존재하는가?
- [ ] 변경된 파일 목록 보여줬는가?
- [ ] 커밋 메시지 확인했는가?
- [ ] push 결과 확인했는가?
