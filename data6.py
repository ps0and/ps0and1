import streamlit as st
def show():
    st.header("🗓️ Day 6")
    st.subheader("인공지능의 이해")
    st.write("AI는 어떻게 생각하는지 알아 봅시다.")
    st.divider()
    st.subheader("🎥 오늘의 수업 영상")
    st.video("https://youtu.be/RYTRvvmHMfI")
    st.subheader("📌 학습 목표")
    st.write("""
    - 수학적 사고와 인공지능적 사고의 차이를 설명할 수 있다.
    - 회귀와 딥러닝의 기본 원리 및 학습 과정을 이해한다.
    """)
    st.divider()
        # 📘 주제 1
    with st.expander("📘 주제 1: 수학적 사고 vs 인공지능적 사고", expanded=True):
        st.markdown("""
        수학자는 문제를 보고 스스로 규칙을 찾아내고, 이를 식으로 표현합니다.  
        예를 들어 `2, 4, 6, ...`이라는 수열을 보면 “`2`씩 증가하는 규칙이네”라고 판단하고 $a_n = 2n$이라는 식을 세웁니다. 이는 인간의 직관과 논리를 활용한 방식이죠.

        하지만 인공지능(AI)은 사람처럼 사고하지 않고, 많은 숫자 데이터를 관찰하여 그 안에 숨어 있는 규칙을 자동으로 찾아냅니다. 예를 들어 아래와 같은 데이터를 보고:
            """)
            # 테이블 대신 목록으로 전개
        st.markdown("""
        - `x` (항 번호): `1` → `y` (수열 값): `2`  
        - `x` (항 번호): `2` → `y` (수열 값): `4`  
        - `x` (항 번호): `3` → `y` (수열 값): `6`
        - `x` (항 번호): `4` → `y` (수열 값): `8`  
            """)
        st.markdown("""
        AI는 “`x`가 `1`씩 증가할 때 `y`는 `2`씩 증가하네 → $y = 2x$”라는 규칙을 스스로 찾아냅니다.

        👉 [두 줄 정리]
        - **수학자**는 규칙을 **직접 생각**  
        - **AI**는 규칙을 **데이터로부터 학습**합니다.
            """)
        # 📊 주제 2
    with st.expander("📊 주제 2: AI는 어떻게 학습할까? — 회귀와 함수의 원리", expanded=True):
        st.markdown("""
        - AI는 숫자들 사이의 관계를 수학적으로 표현하는 법을 학습합니다.  
        가장 기본적인 방식이 **회귀**(regression)입니다. 회귀는 입력값 $x$와 출력값 $y$ 사이의 관계를 함수 형태로 표현하는 것이며, 대표적으로 **선형 회귀**(linear regression)가 있습니다.
        """)
        col1, col2 = st.columns([1, 1])  # 비율을 조정할 수 있음
        with col1:
            st.image("image/1dim.png",
                    caption="선형회귀",
                    width=300)  # 이미지 크기 조정 가능
        with col2:
            st.latex(r"y = ax + b")
            st.markdown("""예를 들어, 아래와 같은 데이터를 AI가 관찰했다면: `x: 1 → y: 3 , x: 2 → y: 5 , x: 3 → y: 7` 
            이 데이터를 통해 AI는 수식을 $y = 2x + 1$로 학습할 수 있습니다.  이처럼 선형 회귀는 **직선으로 표현 가능한 관계**를 찾아내는 방법입니다.""")
        col1, col2 = st.columns([1, 1])  # 비율을 조정할 수 있음
        with col1:
            st.image("image/2dim.png",
                    caption="다항회귀",
                    width=300)  # 이미지 크기 조정 가능
        with col2:
            st.markdown("""
            하지만 어떤 데이터는 **직선이 아니라 곡선**으로 표현됩니다. 예를 들어: ` x: 1 → y: 1, x: 2 → y: 4, x: 3 → y: 9` 이 관계는 $y = x^2$이라는 **2차 함수**로 설명할 수 있고, 이는 **다항 회귀**(polynomial regression)를 통해 학습됩니다.
            """)
            st.latex(r"y = ax^2 + bx + c")
        st.markdown("""
        - 여기서 **차수**(degree)는 함수의 최고 차항을 의미하며, 차수가 높아질수록 더 복잡한 패턴도 설명할 수 있습니다.
        
        👉 [두 줄 정리]
        - **선형 회귀**는 입력과 출력 사이의 직선 규칙을 찾는 방법
        - **다항 회귀**는 데이터의 곡선 패턴까지 학습할 수 있음
        """)

        # 📐 주제 3
    with st.expander("📐 주제 3: AI는 수식을 어떻게 만들까? — 반복 학습과 오차 최소화"):
        st.markdown("""
        AI는 수식을 스스로 만들기 위해 수많은 수식 조합을 시도해봅니다. 예를 들어 아래와 같은 형태의 수식을 가정합니다
        """)

        col1, col2 = st.columns([1, 1])  # 비율을 조정할 수 있음
        with col1:
            st.image("image/sleep.png",
                    caption="AI가 수식을 찾는 과정",
                    width=300)  # 이미지 크기 조정 가능
        with col2:
            st.latex(r"y = w_1x + w_0")        
            st.markdown("""
            이때 $w_1$과 $w_0$는 AI가 학습을 통해 찾아내는 **계수**(weight)입니다. AI는 다양한 값을 시도해보며, **예측값과 실제값의 차이**를 줄이려고 합니다.
            이 오차를 계산하는 방법 중 하나가 **평균제곱오차**(MSE: Mean Squared Error)입니다:
            """)
        st.latex(r"\text{MSE} = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2")
        st.markdown("""
        - $y_i$: 실제값 , $\hat{y}_i$: 예측값  

        AI는 이 오차를 **가장 작게** 만드는 방향으로 수식의 계수를 계속 수정합니다. 이 과정을 **반복 학습**(iterative learning)이라고 하며, 사람이 수식을 직접 세우는 것과 달리 AI는 ‘**시도와 오차 줄이기**’를 통해 최적의 수식을 찾아냅니다.
        
        👉 [두 줄 정리]
        - AI는 **예측값**과 **실제값**의 차이(오차)를 계산해서 오차가 **작아**지도록 수식의 **계수**를 반복해서 **수정**하며 **학습**합니다.                 
        """)

        # 🧠 주제 4
    with st.expander("🧠 주제 4: 딥러닝 구조와 반복 학습의 특징"):
        st.markdown("""AI가 더욱 복잡한 문제를 해결하기 위해 발전한 기술이 **딥러닝**(Deep Learning)입니다.
        딥러닝은 **인공신경망**(Artificial Neural Network)을 기반으로 하며,
        사람의 뇌 구조를 모방하여 정보를 처리합니다.
        딥러닝은 입력값을 받아 여러 단계(층)를 거치며 출력값을 생성합니다.
        """)
        col1, col2 = st.columns([1, 1])  # 비율을 조정할 수 있음
        with col1:
            st.image("image/deep_learning_structure.png",
                    caption="딥러닝 구조 예시",
                    width=300)  # 이미지 크기 조정 가능

        with col2:
            st.markdown("""
            ##### 🔗 딥러닝 구조:
            입력층 → 은닉층(hidden layer) → 출력층
            각 층에는 수많은 **뉴런**(neuron)이 존재하고, 이들은 정보를 조금씩 처리하며 다음 층으로 전달합니다.  
            층이 많아질수록 복잡한 패턴을 인식할 수 있으며, 뉴런 수가 많을수록 더 정교한 정보 표현이 가능합니다.
            """)    
        st.markdown("""
        ##### 🔁 반복 학습과 에포크(epoch)

        이러한 딥러닝 모델은 데이터를 여러 번 학습하면서 성능을 높입니다. **에포크**(epoch)란 **전체 데이터를 한 번 학습하는 과정**을 말합니다. 에포크가 반복될수록 AI는 오차를 줄이며 더 정확한 예측을 하게 됩니다.
                    
        👉 **[두 줄 정리]**
        - **딥러닝**은 여러 층을 거치며 복잡한 패턴까지 찾아내는 AI 방법
        - **데이터**를 여러 번 **학습**(에포크)해 오차를 점점 줄여간다
        """)

        # 📌 주제 5
    with st.expander("📌 주제 5: 수학 모델 vs AI 모델 — 공통점과 차이점"):
        st.markdown("""
        수학 모델과 AI 모델은 모두 **규칙을 표현하는 방식**이지만, 그 접근법과 장단점이 다릅니다.
        """)
        st.table({
                "구분": ["규칙 생성", "해석 용이성", "적용 대상"],
                "수학 모델": [
                    "사람이 직접 공식을 만든다",
                    "직관적으로 쉽게 이해할 수 있다",
                    "규칙이 명확한 문제에 적합"
                ],
                "AI 모델": [
                    "데이터를 통해 규칙을 자동으로 찾는다",
                    "식은 복잡하고 해석이 어려울 수 있다",
                    "복잡하고 불확실한 문제에 적합"
                ]
            })
        st.markdown("""
        예를 들어, 수학자는 수열을 보고 $a_n = 2n$이라는 공식을 만들 수 있습니다.  
        하지만 AI는 항 번호와 값만 보고 그 관계를 **수치적으로 학습**하여 $y = 2x$라는 수식을 찾아냅니다.

        수학 모델은 해석과 설명이 용이하지만 복잡한 현실 데이터를 다루는 데 한계가 있고,  
        AI 모델은 복잡한 문제를 잘 해결하지만 내부 작동 원리가 직관적으로 보이지 않는다는 단점이 있습니다.

        🎯 결국 두 방식은 상호 보완적이며,  
        **21세기 수학 교육에서는 이 두 접근을 모두 익히는 것이 중요**합니다.
        """)
    st.divider()
    st.markdown("##### 🌈 :rainbow[[수준별 문제]] AI 개념 확인")

    ai_level = st.radio(
        "난이도를 선택하세요!",
        ("하", "중", "상"),
        horizontal=True,
        key="d6_ai_level"
    )

    if ai_level == "하":
        q_title = "수학적 사고와 AI 사고의 차이"
        q_question = "AI는 데이터를 통해 규칙을 ( )합니다. (빈칸에 들어갈 한 단어를 입력하세요)"
        correct_word = "학습"
        st.markdown(f"**[{ai_level}] {q_title}**")
        st.write(q_question)
        user_word = st.text_input("✏️ 한 단어 입력", key="d6_word_ans")
        if user_word:
            if user_word.strip().lower() == correct_word.lower():
                st.success("정답입니다! 🎉")
            else:
                st.error("정답이 아닙니다. 다시 생각해 보세요.")
        with st.expander("💡 정답 보기"):
            st.markdown(f"정답: **{correct_word}**")

    elif ai_level == "중":
        q_title = "회귀와 학습"
        q_question = "AI가 선형 회귀로 예측 모델을 학습할 때 반복적으로 수행하는 것은 무엇인가요?"
        options = [
            "① 다양한 수식을 무작위로 만든다.",
            "② 예측값과 실제값의 오차를 계산하고, 오차를 줄이도록 계수를 반복 수정한다.",
            "③ 정답을 미리 입력받아 암기한다.",
            "④ 데이터를 그대로 출력한다."
        ]
        sample_answer = options[1]
        st.markdown(f"**[{ai_level}] {q_title}**")
        st.write(q_question)
        user_choice = st.radio("정답을 선택하세요.", options, key="d6_choice")
        if user_choice == sample_answer:
            st.success("정답입니다! 🎉")
        elif user_choice:
            st.error("정답이 아닙니다.")
        with st.expander("💡 정답 보기"):
            st.markdown(f"**정답:** {sample_answer}")

    else:  # 상
        q_title = "수학 모델과 AI 모델의 차이"
        q_question = "수학 모델과 AI 모델의 차이를 2문장 이상으로 설명해 보세요."
        sample_answer = (
            "수학 모델은 사람이 직접 공식을 만들고 해석이 쉽지만, 복잡한 데이터에는 한계가 있습니다. "
            "AI 모델은 데이터에서 규칙을 자동으로 학습해 복잡한 문제에 잘 대응하지만 해석이 어려울 수 있습니다."
        )
        st.markdown(f"**[{ai_level}] {q_title}**")
        st.write(q_question)
        user_answer = st.text_area("✏️ 답을 입력해 보세요.", height=80, key="d6_long_ans")
        # 상은 정답 체크 없이 예시 제공
        with st.expander("💡 모범 답안 보기"):
            st.markdown(sample_answer)
