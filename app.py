import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Color Match Game | GlobalInternet.py",
    page_icon="🎨",
    layout="wide"
)

# ---------- CUSTOM CSS (dark, kid-friendly) ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
        border-right: 2px solid #e94560;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
        color: #ffffff !important;
    }
    .stButton button {
        background-color: #e94560 !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.2s;
    }
    .stButton button:hover {
        background-color: #ff6b6b !important;
        transform: scale(1.02);
    }
    h1, h2, h3 {
        color: #ffd966 !important;
    }
    p, li, .stMarkdown, .stCaption, .footer {
        color: #ffffff !important;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #e94560;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SPINNING GLOBE ----------
def spinning_globe():
    st.sidebar.markdown("""
    <div style="text-align: center;">
        <div style="font-size:80px; animation:spin 4s linear infinite; display:inline-block;">🎨</div>
    </div>
    <style>
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# ---------- SIDEBAR (no pricing, built by Gesner) ----------
def show_sidebar():
    spinning_globe()
    st.sidebar.markdown("## **GlobalInternet.py**")
    st.sidebar.markdown("### 🎨 Color Match Game")
    st.sidebar.markdown("Match each color swatch with its correct name!")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Built by Gesner Deslandes** – Coder in Chief")
    st.sidebar.markdown("📞 (509)-47385663")
    st.sidebar.markdown("✉️ deslandes78@gmail.com")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🌐 Website:**")
    st.sidebar.markdown("[https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎮 How to Play")
    st.sidebar.markdown("1. Drag a color name (bottom row) to its matching color swatch (top row).")
    st.sidebar.markdown("2. Hear a **Bingo!** sound when correct.")
    st.sidebar.markdown("3. Match all colors to see **balloons fly** and hear a victory fanfare!")
    st.sidebar.markdown("4. Use **Reset Game** to shuffle and play again.")
    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Reset Game", use_container_width=True):
        st.rerun()

# ---------- COLOR MATCHING GAME (drag & drop) ----------
def color_match_game():
    game_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <style>
            * {
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }
            body {
                background: transparent;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 0.5rem;
            }
            .game-container {
                background: rgba(0,0,0,0.3);
                border-radius: 30px;
                padding: 1.5rem;
            }
            .game-title {
                text-align: center;
                margin-bottom: 1rem;
            }
            .game-title h2 {
                color: #ffd966;
                margin: 0;
            }
            .game-title p {
                color: #ddd;
                font-size: 1rem;
            }
            .colors-row {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                margin: 20px 0 30px;
                padding: 15px;
                background: rgba(255,255,255,0.05);
                border-radius: 40px;
                min-height: 160px;
            }
            .color-swatch {
                width: 110px;
                height: 110px;
                border-radius: 20px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.3);
                transition: transform 0.2s, box-shadow 0.2s;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: default;
                border: 3px solid rgba(255,255,255,0.6);
                position: relative;
            }
            .color-swatch.matched {
                opacity: 0.8;
                border: 3px solid gold;
                box-shadow: 0 0 15px gold;
                transform: scale(0.98);
            }
            .color-swatch .check-mark {
                font-size: 48px;
                font-weight: bold;
                color: white;
                text-shadow: 2px 2px 4px black;
                display: none;
            }
            .color-swatch.matched .check-mark {
                display: block;
            }
            .names-row {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 15px;
                margin: 20px 0;
                padding: 15px;
                background: rgba(0,0,0,0.4);
                border-radius: 40px;
                min-height: 90px;
            }
            .draggable-name {
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                color: #1a1a2e;
                font-weight: bold;
                font-size: 1.3rem;
                padding: 12px 24px;
                border-radius: 60px;
                cursor: grab;
                transition: all 0.2s;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                text-align: center;
                min-width: 90px;
                letter-spacing: 1px;
            }
            .draggable-name:active {
                cursor: grabbing;
            }
            .draggable-name.dragging {
                opacity: 0.4;
                cursor: grabbing;
            }
            .draggable-name:hover {
                transform: scale(1.05);
                background: #ff6b6b;
                color: white;
            }
            .info-panel {
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 15px;
                margin-top: 20px;
                background: rgba(0,0,0,0.5);
                padding: 10px 20px;
                border-radius: 40px;
            }
            .remaining {
                color: white;
                font-weight: bold;
                font-size: 1.2rem;
                background: #e94560;
                padding: 6px 16px;
                border-radius: 40px;
            }
            .reset-btn {
                background-color: #e94560;
                color: white;
                border: none;
                border-radius: 40px;
                padding: 10px 28px;
                font-weight: bold;
                font-size: 1rem;
                cursor: pointer;
                transition: 0.2s;
            }
            .reset-btn:hover {
                background-color: #ff6b6b;
                transform: scale(1.02);
            }
            .win-message {
                text-align: center;
                font-size: 2rem;
                font-weight: bold;
                color: #ffd966;
                animation: pulse 0.8s infinite;
                margin: 20px 0;
            }
            @keyframes pulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.05); opacity: 0.8; }
                100% { transform: scale(1); opacity: 1; }
            }
            .error-toast {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                background: #e94560;
                color: white;
                padding: 10px 20px;
                border-radius: 50px;
                font-weight: bold;
                pointer-events: none;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.2s;
                font-size: 1.2rem;
            }
            @media (max-width: 700px) {
                .color-swatch { width: 70px; height: 70px; }
                .draggable-name { padding: 8px 16px; font-size: 1rem; min-width: 70px; }
                .check-mark { font-size: 32px; }
            }
        </style>
    </head>
    <body>
    <div class="game-container">
        <div class="game-title">
            <h2>🎨 Match the Colors! 🎨</h2>
            <p>Drag the color name from the bottom row and drop it onto the matching color swatch above.</p>
        </div>

        <div id="colorsContainer" class="colors-row"></div>
        <div id="namesContainer" class="names-row"></div>

        <div class="info-panel">
            <span class="remaining">🎯 Remaining: <span id="remainingCount">0</span></span>
            <button class="reset-btn" id="resetBtn">🔄 New Game (Shuffle Colors)</button>
        </div>
        <div id="winMessage" style="display: none;" class="win-message">🎉 YOU WIN! 🎉</div>
    </div>
    <div id="errorToast" class="error-toast">❌ Oops! Wrong match, try again!</div>

    <script>
        // ----- COLOR DATA -----
        const colorsData = [
            { name: "Red", bg: "#E63946", value: "red" },
            { name: "Orange", bg: "#F4A261", value: "orange" },
            { name: "Yellow", bg: "#FFD166", value: "yellow" },
            { name: "Green", bg: "#2A9D8F", value: "green" },
            { name: "Blue", bg: "#457B9D", value: "blue" },
            { name: "Purple", bg: "#9B5DE5", value: "purple" },
            { name: "Pink", bg: "#FF85A1", value: "pink" },
            { name: "Brown", bg: "#7F4F24", value: "brown" }
        ];
        const totalColors = colorsData.length;

        // Game state
        let shuffledColors = [];        // shuffled order of colorsData
        let matchedStates = new Array(totalColors).fill(false);
        let remainingMatches = totalColors;
        let winTriggered = false;

        const colorsContainer = document.getElementById('colorsContainer');
        const namesContainer = document.getElementById('namesContainer');
        const remainingSpan = document.getElementById('remainingCount');
        const winDiv = document.getElementById('winMessage');
        const errorToast = document.getElementById('errorToast');
        const resetBtn = document.getElementById('resetBtn');

        let audioCtx = null;
        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            return audioCtx;
        }

        function playBingoSound() {
            const ctx = initAudio();
            ctx.resume().then(() => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.frequency.value = 880;
                gain.gain.value = 0.25;
                osc.type = 'sine';
                gain.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 0.7);
                osc.start();
                osc.stop(ctx.currentTime + 0.7);
            }).catch(e => console.log("Audio error", e));
        }

        function playErrorSound() {
            const ctx = initAudio();
            ctx.resume().then(() => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.frequency.value = 220;
                gain.gain.value = 0.2;
                osc.type = 'square';
                gain.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 0.5);
                osc.start();
                osc.stop(ctx.currentTime + 0.5);
            }).catch(e => console.log("Audio error", e));
        }

        function playWinFanfare() {
            const ctx = initAudio();
            ctx.resume().then(() => {
                const osc1 = ctx.createOscillator();
                const gain1 = ctx.createGain();
                osc1.connect(gain1);
                gain1.connect(ctx.destination);
                osc1.frequency.value = 1046.5;
                gain1.gain.value = 0.3;
                osc1.type = 'sine';
                gain1.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 0.5);
                osc1.start();
                osc1.stop(ctx.currentTime + 0.4);

                const osc2 = ctx.createOscillator();
                const gain2 = ctx.createGain();
                osc2.connect(gain2);
                gain2.connect(ctx.destination);
                osc2.frequency.value = 1318.52;
                gain2.gain.value = 0.3;
                osc2.type = 'sine';
                gain2.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 0.9);
                osc2.start(ctx.currentTime + 0.45);
                osc2.stop(ctx.currentTime + 0.9);
            }).catch(e => console.log("Audio error", e));
        }

        function showErrorToastMsg() {
            errorToast.style.opacity = '1';
            setTimeout(() => { errorToast.style.opacity = '0'; }, 1200);
        }

        function updateRemainingUI() {
            remainingSpan.innerText = remainingMatches;
        }

        function shuffleArray(arr) {
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
            return arr;
        }

        function initGame() {
            shuffledColors = shuffleArray([...colorsData]);
            matchedStates.fill(false);
            remainingMatches = totalColors;
            winTriggered = false;
            winDiv.style.display = 'none';
            updateRemainingUI();
            renderColors();
            renderDraggableNames();
        }

        function renderColors() {
            colorsContainer.innerHTML = '';
            for (let i = 0; i < totalColors; i++) {
                const color = shuffledColors[i];
                const swatch = document.createElement('div');
                swatch.className = 'color-swatch';
                if (matchedStates[i]) swatch.classList.add('matched');
                swatch.style.backgroundColor = color.bg;
                swatch.setAttribute('data-index', i);
                swatch.setAttribute('data-color-name', color.name);
                const checkSpan = document.createElement('div');
                checkSpan.className = 'check-mark';
                checkSpan.innerText = '✓';
                swatch.appendChild(checkSpan);
                
                swatch.addEventListener('dragover', (e) => e.preventDefault());
                swatch.addEventListener('drop', (e) => {
                    e.preventDefault();
                    if (winTriggered) return;
                    const swatchIndex = parseInt(e.currentTarget.getAttribute('data-index'));
                    if (matchedStates[swatchIndex]) return;
                    
                    const draggedColorName = e.dataTransfer.getData('text/plain');
                    if (!draggedColorName) return;
                    
                    const targetColorName = shuffledColors[swatchIndex].name;
                    if (draggedColorName === targetColorName) {
                        playBingoSound();
                        matchedStates[swatchIndex] = true;
                        remainingMatches--;
                        updateRemainingUI();
                        e.currentTarget.classList.add('matched');
                        const targetDraggable = document.querySelector(`.draggable-name[data-color-name="${draggedColorName}"]`);
                        if (targetDraggable) targetDraggable.remove();
                        if (remainingMatches === 0 && !winTriggered) {
                            winTriggered = true;
                            winDiv.style.display = 'block';
                            playWinFanfare();
                            launchBalloonsCelebration();
                        }
                    } else {
                        playErrorSound();
                        showErrorToastMsg();
                    }
                });
                colorsContainer.appendChild(swatch);
            }
        }

        function renderDraggableNames() {
            namesContainer.innerHTML = '';
            for (let i = 0; i < totalColors; i++) {
                if (!matchedStates[i]) {
                    const color = shuffledColors[i];
                    const dragItem = document.createElement('div');
                    dragItem.className = 'draggable-name';
                    dragItem.innerText = color.name;
                    dragItem.setAttribute('data-color-name', color.name);
                    dragItem.setAttribute('draggable', 'true');
                    
                    dragItem.addEventListener('dragstart', (e) => {
                        e.dataTransfer.setData('text/plain', color.name);
                        e.dataTransfer.effectAllowed = 'move';
                        e.target.classList.add('dragging');
                    });
                    dragItem.addEventListener('dragend', (e) => {
                        e.target.classList.remove('dragging');
                    });
                    namesContainer.appendChild(dragItem);
                }
            }
        }

        function launchBalloonsCelebration() {
            const container = document.createElement('div');
            container.style.position = 'fixed';
            container.style.top = '0';
            container.style.left = '0';
            container.style.width = '100%';
            container.style.height = '100%';
            container.style.pointerEvents = 'none';
            container.style.zIndex = '10000';
            document.body.appendChild(container);
            
            for (let i = 0; i < 100; i++) {
                const balloon = document.createElement('div');
                balloon.style.position = 'absolute';
                balloon.style.bottom = '-50px';
                balloon.style.left = Math.random() * 100 + '%';
                balloon.style.width = '45px';
                balloon.style.height = '55px';
                balloon.style.backgroundColor = `hsl(${Math.random() * 360}, 80%, 60%)`;
                balloon.style.borderRadius = '50%';
                balloon.style.animation = `floatUp ${4 + Math.random() * 3}s linear forwards`;
                balloon.style.fontSize = '28px';
                balloon.style.textAlign = 'center';
                balloon.style.lineHeight = '55px';
                balloon.innerHTML = '🎈';
                container.appendChild(balloon);
            }
            
            for (let i = 0; i < 120; i++) {
                const star = document.createElement('div');
                star.style.position = 'absolute';
                star.style.bottom = '-20px';
                star.style.left = Math.random() * 100 + '%';
                star.style.width = '8px';
                star.style.height = '8px';
                star.style.backgroundColor = '#FFD966';
                star.style.borderRadius = '50%';
                star.style.animation = `floatUp ${3 + Math.random() * 2}s linear forwards`;
                star.style.boxShadow = '0 0 8px gold';
                container.appendChild(star);
            }
            
            const winText = document.createElement('div');
            winText.innerText = '🏆 GREAT JOB! 🏆';
            winText.style.position = 'absolute';
            winText.style.bottom = '20%';
            winText.style.left = '50%';
            winText.style.transform = 'translateX(-50%)';
            winText.style.fontSize = '2.5rem';
            winText.style.fontWeight = 'bold';
            winText.style.color = '#FFD966';
            winText.style.textShadow = '2px 2px 10px #e94560';
            winText.style.animation = 'pulse 0.8s infinite';
            winText.style.fontFamily = 'Arial Black, sans-serif';
            container.appendChild(winText);
            
            const creditSpan = document.createElement('div');
            creditSpan.innerText = 'Built by Gesner Deslandes';
            creditSpan.style.position = 'absolute';
            creditSpan.style.bottom = '10px';
            creditSpan.style.right = '20px';
            creditSpan.style.color = 'white';
            creditSpan.style.backgroundColor = 'rgba(0,0,0,0.5)';
            creditSpan.style.padding = '5px 12px';
            creditSpan.style.borderRadius = '30px';
            creditSpan.style.fontSize = '0.9rem';
            creditSpan.style.fontFamily = 'sans-serif';
            container.appendChild(creditSpan);
            
            const style = document.createElement('style');
            style.textContent = `
                @keyframes floatUp {
                    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
                    100% { transform: translateY(-120vh) rotate(20deg); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
            setTimeout(() => { container.remove(); }, 9000);
        }
        
        resetBtn.addEventListener('click', () => initGame());
        initGame();
    </script>
    </body>
    </html>
    """
    components.html(game_html, height=700, scrolling=True)

# ---------- MAIN APP ----------
def main_app():
    show_sidebar()
    
    # Image from GitHub (raw URL) - reduced size, aligned right of title
    image_url = "https://raw.githubusercontent.com/Deslandes1/Color-Software-Game/main/Gesner%20Deslandes.png"
    
    # Two columns: title on left (aligned right), picture on right (small)
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h1 style='text-align:right; margin-bottom:0;'>🎨 Color Match Game 🎨</h1>", unsafe_allow_html=True)
    with col2:
        st.image(image_url, width=60)  # Reduced size
    
    st.markdown("<p style='text-align:center; font-size:1.2rem;'>Drag the color names to the matching colored squares. Listen for the BINGO sound!</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ffd966;'>✨ Built by Gesner Deslandes ✨</p>", unsafe_allow_html=True)
    color_match_game()
    st.markdown('<div class="footer">© GlobalInternet.py – Learning colors is fun! Drag, drop, and match.</div>', unsafe_allow_html=True)

# ---------- DIRECT ACCESS (No login required for kids) ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True

if not st.session_state.authenticated:
    st.markdown("Please refresh")
else:
    main_app()
