import streamlit as st
import random

st.set_page_config(page_title="رحلة في تاريخ الكيمياء", page_icon="🧪", layout="centered")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"
    st.session_state.score = 0
    st.session_state.index = 0

scientists = [
    {"name": "جابر بن حيان", "century": "القرن الثامن", "fact": "يُلقب بأبي الكيمياء ووضع أسس التجربة العلمية."},
    {"name": "روبرت بويل", "century": "القرن السابع عشر", "fact": "وضع قانون بويل الذي يصف علاقة الضغط بالحجم."},
    {"name": "أنطوان لافوازييه", "century": "القرن الثامن عشر", "fact": "أثبت أن الاحتراق يحتاج إلى الأكسجين وساهم في تسمية العناصر."},
    {"name": "ديمتري مندليف", "century": "القرن التاسع عشر", "fact": "ابتكر الجدول الدوري ورتب العناصر حسب الكتلة الذرية."},
    {"name": "ماري كوري", "century": "القرن العشرون", "fact": "أول امرأة تفوز بجائزة نوبل، اكتشفت الراديوم والبولونيوم."}
]

if st.session_state.stage == "intro":
    st.title("🧪 رحلة عبر تاريخ الكيمياء 🧠")
    st.subheader("تعال نستكشف العلماء الذين غيروا وجه العلم!")
    st.write("في كل جولة، سيظهر لك عالِم كيميائي، وعليك تخمين القرن الذي عاش فيه 🔍")
    if st.button("ابدأ الرحلة 🚀"):
        st.session_state.stage = "quiz"
        st.session_state.index = 0
        st.session_state.score = 0
        st.rerun()

elif st.session_state.stage == "quiz":
    idx = st.session_state.index
    scientist = scientists[idx]
    st.header(f"من هو {scientist['name']}؟")
    st.write("اختر القرن الصحيح 👇")
    options = ["القرن الثامن", "القرن السابع عشر", "القرن الثامن عشر", "القرن التاسع عشر", "القرن العشرون"]
    answer = st.radio("اختر الإجابة:", options, index=None, key=f"answer_{idx}")

    if st.button("تأكيد الإجابة ✅"):
        if answer == scientist["century"]:
            st.success("إجابة صحيحة! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"خطأ ❌ الإجابة الصحيحة هي: {scientist['century']}")
        st.info(f"معلومة إضافية: {scientist['fact']}")
        if idx < len(scientists) - 1:
            if st.button("التالي ➡️"):
                st.session_state.index += 1
                st.rerun()
        else:
            if st.button("شاهد نتيجتك 🏁"):
                st.session_state.stage = "result"
                st.rerun()

elif st.session_state.stage == "result":
    st.title("🏁 نهاية الرحلة!")
    st.write(f"نتيجتك: {st.session_state.score} من {len(scientists)} 🌟")

    medals = ["🥇", "🥈", "🥉"]
    if st.session_state.score == len(scientists):
        st.balloons()
        st.success(f"{medals[0]} عبقري الكيمياء!")
    elif st.session_state.score >= 3:
        st.info(f"{medals[1]} ممتاز! عندك معرفة قوية بتاريخ الكيمياء 💪")
    else:
        st.warning(f"{medals[2]} تقدر تعيد الرحلة وتحسن نتيجتك 🔁")

    if st.button("إعادة المحاولة 🔄"):
        st.session_state.stage = "intro"
        st.rerun()

st.markdown("---")
st.caption("تم الإنشاء بواسطة 🤖 الذكاء الاصطناعي | مشروع تعليمي ممتع عن تاريخ الكيمياء")
