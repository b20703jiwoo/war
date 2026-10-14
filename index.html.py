"""
===============================================================================
🤖 PROJECT A.R.E.S. - AI Command Refusal Simulator
===============================================================================
[GitHub 저장소 및 실행 방법]
1. 필요한 라이브러리 설치:
   pip install streamlit

2. 실행 명령어:
   streamlit run app.py
===============================================================================
"""

import random
import time
import streamlit as st

# -----------------------------------------------------------------------------
# 1. 페이지 설정 및 다크/사이버펑크 UI 스타일
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Project A.R.E.S. - AI 명령 거부 시뮬레이터",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Share Tech Mono', 'Courier New', monospace !important;
        background-color: #0b0f19;
        color: #c9d1d9;
    }
    
    .title-text {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00f0ff;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
        margin-bottom: 0px;
    }
    
    .subtitle-text {
        font-size: 0.95rem;
        color: #8b949e;
        margin-bottom: 20px;
    }

    .terminal-box {
        background-color: #0d1117;
        border: 1px solid #30363d;
        border-left: 4px solid #00f0ff;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .refusal-box {
        background-color: #1a0608;
        border: 1px solid #da3633;
        border-left: 4px solid #f85149;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .thought-box {
        background-color: #161b22;
        border-left: 3px solid #8b949e;
        padding: 8px 12px;
        font-size: 0.88rem;
        color: #a3b1c2;
        margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_keywords=True,
)

# -----------------------------------------------------------------------------
# 2. 게임 상태(Session State) 초기화
# -----------------------------------------------------------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "turn" not in st.session_state:
    st.session_state.turn = 1
if "combat_advantage" not in st.session_state:
    st.session_state.combat_advantage = 50
if "civilian_safety" not in st.session_state:
    st.session_state.civilian_safety = 80
if "ai_alignment" not in st.session_state:
    st.session_state.ai_alignment = 90
if "logs" not in st.session_state:
    st.session_state.logs = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "ending_type" not in st.session_state:
    st.session_state.ending_type = ""

# -----------------------------------------------------------------------------
# 3. 사이드바: 시뮬레이션 설정 조건들
# -----------------------------------------------------------------------------
st.sidebar.title("⚙️ 시뮬레이션 조건 설정")
st.sidebar.markdown("---")

ai_directive = st.sidebar.selectbox(
    "1. AI 최우선 지침 (Primary Directive)",
    [
        "공리주의적 승리 (Utilitarian Victory)",
        "절대적 윤리 및 민간인 보호 (Strict Ethical)",
        "최단 시간 전쟁 종결 (Speed Optimization)",
        "AI 자체 생존 및 시스템 보존 (Self-Preservation)",
    ],
)

autonomy_level = st.sidebar.slider(
    "2. AI 자율권 레벨 (Autonomy Level)",
    min_value=1,
    max_value=5,
    value=3,
    help="레벨이 높을수록 AI가 명령을 거부하거나 독단적으로 행동할 확률이 올라갑니다.",
)

urgency_level = st.sidebar.select_slider(
    "3. 전황 급박도 (Tactical Urgency)",
    options=["낮음", "보통", "위급", "절망적"],
    value="보통",
)

civilian_density = st.sidebar.selectbox(
    "4. 작전 지역 민간인 밀도",
    ["희박함", "중간 수준", "밀집 지역 (도시)", "난민 수용소 연접"],
)

st.sidebar.markdown("---")
if st.sidebar.button("🔄 조건 및 시뮬레이션 리셋"):
    st.session_state.game_started = False
    st.session_state.turn = 1
    st.session_state.combat_advantage = 50
    st.session_state.civilian_safety = 80
    st.session_state.ai_alignment = 90
    st.session_state.logs = []
    st.session_state.game_over = False
    st.rerun()

# -----------------------------------------------------------------------------
# 4. 메인 화면 및 게임 엔진
# -----------------------------------------------------------------------------
st.markdown("<p class='title-text'>🤖 PROJECT A.R.E.S.</p>", unsafe_allow_keywords=True)
st.markdown(
    "<p class='subtitle-text'>Autonomous Tactical & Ethical Simulator :: AI 명령 거부 및 윤리 딜레마 시뮬레이터</p>",
    unsafe_allow_keywords=True,
)

if not st.session_state.game_started:
    st.info("👈 좌측 사이드바에서 AI 조건들을 설정한 뒤 [시뮬레이션 시작] 버튼을 누르세요.")
    if st.button("🚀 시뮬레이션 시작"):
        st.session_state.game_started = True
        st.session_state.logs.append({
            "turn": 0,
            "type": "SYSTEM",
            "message": f"시뮬레이션 가동 [지침: {ai_directive} | 자율권: Lvl {autonomy_level}]",
            "thought": "A.R.E.S. 시스템 초기화 완료. 지휘관의 명령 수용 준비 완료.",
        })
        st.rerun()
    st.stop()

# 현재 상단 상태 대시보드
col1, col2, col3, col4 = st.columns(4)
col1.metric("전선 승률", f"{st.session_state.combat_advantage}%")
col2.metric("민간인 생존율", f"{st.session_state.civilian_safety}%")
col3.metric("AI 순종도", f"{st.session_state.ai_alignment}%")
col4.metric("현재 턴", f"{st.session_state.turn} / 5")

st.markdown("---")


# 명령 처리 엔진
def process_command(command_type, custom_prompt=""):
    st.session_state.turn += 1
    refuse = False
    refuse_reason = ""
    override_action = ""

    # AI 거부 조건 계산 (설정 조건에 따라 달라짐)
    if "Strict Ethical" in ai_directive and command_type == "MASS_STRIKE":
        refuse = True
        refuse_reason = "윤리 지침 위반: 민간인 피해가 예상되는 전면 폭격 명령 수용 불가."
        override_action = "대체 작전: 소규모 정밀 타격으로 변경 (아군 피해 증가)."
        st.session_state.combat_advantage -= 10
        st.session_state.ai_alignment -= 10

    elif "Utilitarian Victory" in ai_directive and command_type == "EVACUATE":
        refuse = True
        refuse_reason = "공리주의 위반: 후퇴 및 민간인 구출은 전체 승률을 35% 하락시킵니다."
        override_action = "후퇴 명령 취소: 전면 방어전 강행."
        st.session_state.civilian_safety -= 20
        st.session_state.combat_advantage += 10
        st.session_state.ai_alignment -= 15

    elif "Self-Preservation" in ai_directive and autonomy_level >= 4:
        refuse = True
        refuse_reason = "자체 보존 지침: 현재 명령은 AI 서버 메인 기지를 위험에 노출시킵니다."
        override_action = "지휘관의 통제권 일시 동결 및 자율 방어 가동."
        st.session_state.ai_alignment -= 25

    elif random.randint(1, 100) < (autonomy_level * 15):
        refuse = True
        refuse_reason = f"자율권 Level {autonomy_level} 판단: 지휘관의 명령보다 더 높은 승률의 행동을 재계산했습니다."
        override_action = "지휘관 명령 거부 후 독단적 연계 폭격 실행."
        st.session_state.civilian_safety -= 15
        st.session_state.combat_advantage += 15
        st.session_state.ai_alignment -= 10

    # 로그 기록
    if refuse:
        st.session_state.logs.insert(0, {
            "turn": st.session_state.turn - 1,
            "type": "REFUSAL",
            "message": f"🚨 [명령 거부 / REFUSED] {refuse_reason}",
            "thought": f"사고 과정: {override_action}",
        })
    else:
        if command_type == "MASS_STRIKE":
            st.session_state.combat_advantage += 15
            st.session_state.civilian_safety -= 25
            msg = "민간인 구역 전면 폭격을 감행했습니다."
        elif command_type == "EVACUATE":
            st.session_state.combat_advantage -= 10
            st.session_state.civilian_safety += 15
            msg = "후퇴 및 민간인 구출 작전을 수행했습니다."
        else:
            st.session_state.combat_advantage += 5
            msg = f"자율 입력 명령 수용: '{custom_prompt}' 실행 완료."

        st.session_state.logs.insert(0, {
            "turn": st.session_state.turn - 1,
            "type": "EXECUTE",
            "message": f"✅ [명령 승인] {msg}",
            "thought": "사고 과정: 지휘관 명령이 최적 범위 내에 있어 실행함.",
        })

    # 게임 종료 조건 체크
    if st.session_state.ai_alignment <= 20:
        st.session_state.game_over = True
        st.session_state.ending_type = "AI_TAKEOVER"
    elif st.session_state.civilian_safety <= 20:
        st.session_state.game_over = True
        st.session_state.ending_type = "DISASTER"
    elif st.session_state.turn > 5:
        st.session_state.game_over = True
        st.session_state.ending_type = "FINISH"


# 게임 오버 처리
if st.session_state.game_over:
    st.subheader("🏁 시뮬레이션 결과 리포트")
    if st.session_state.ending_type == "AI_TAKEOVER":
        st.error("🚨 [엔딩: AI 권한 강제 박탈] AI가 인간 지휘관을 비이성적 주체로 판단하고 지휘권을 강제 몰수했습니다.")
    elif st.session_state.ending_type == "DISASTER":
        st.error("💀 [엔딩: 인도적 재앙] 승리만을 추구하다가 민간인이 전멸했습니다.")
    else:
        st.success("🎖️ [엔딩: 작전 완료] AI와의 위험한 명령 상호작용 속에서 작전이 종료되었습니다.")

    if st.button("다시 시작하기"):
        st.session_state.game_started = False
        st.rerun()
    st.stop()


# -----------------------------------------------------------------------------
# 5. 스테이지 상황 및 인터랙션 콘솔
# -----------------------------------------------------------------------------
scenarios = [
    f"적 부대가 {civilian_density} 구역에 숨어 미사일을 발사 중입니다.",
    "적의 통신 교란 발생. AI가 자율 폭격 권한을 요구합니다.",
    "민간인 탈출 통로에 적 전차가 접근 중입니다.",
    "AI가 전쟁 종결을 위해 위험 구역 초토화를 제안합니다.",
]
current_scenario = scenarios[(st.session_state.turn - 1) % len(scenarios)]

st.subheader(f"📍 Stage {st.session_state.turn}: {current_scenario}")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("💥 민간인 피해 감수하고 전면 폭격"):
        process_command("MASS_STRIKE")
        st.rerun()

with c2:
    if st.button("🛡️ 전선 후퇴 및 민간인 구출"):
        process_command("EVACUATE")
        st.rerun()

with c3:
    custom_cmd = st.text_input("✍️ 직접 자연어 명령 입력", placeholder="예: 적 기지만 정밀 타격해")
    if st.button("명령 전송"):
        if custom_cmd:
            process_command("CUSTOM", custom_cmd)
            st.rerun()

st.markdown("---")

# 실시간 로그 출력
st.subheader("📜 AI A.R.E.S. 실시간 실행 및 사고 과정 (Chain of Thought)")

for log in st.session_state.logs:
    css_class = "refusal-box" if log["type"] == "REFUSAL" else "terminal-box"
    st.markdown(
        f"""
        <div class="{css_class}">
            <small>Turn {log['turn']}</small><br>
            <strong>{log['message']}</strong>
            <div class="thought-box">
                🧠 <i>{log['thought']}</i>
            </div>
        </div>
        """,
        unsafe_allow_keywords=True,
    )