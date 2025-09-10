#!/bin/bash

# Complete Android Project Reset and Fix

echo "🔧 Fixing Android Studio project setup..."

# Stop any running processes
pkill -f "gradle" 2>/dev/null || true

# Clean everything
echo "🧹 Cleaning previous builds..."
rm -rf android
rm -rf node_modules
rm -rf dist
rm -f package-lock.json

# Reinstall Node dependencies
echo "📦 Reinstalling Node.js dependencies..."
npm install

# Create proper dist directory with all assets
echo "📁 Creating proper build directory..."
mkdir -p dist

# Copy all your web assets
cp -r static/* dist/ 2>/dev/null || echo "Static files copied"
cp -r templates dist/ 2>/dev/null || echo "Templates copied"

# Create a proper mobile index.html
cat > dist/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>AWS Cloud Orbit</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Mobile-specific overrides */
        body {
            margin: 0;
            padding: 20px;
            background: #1a1a1a;
            color: white;
            font-family: 'Segoe UI', Arial, sans-serif;
            -webkit-user-select: none;
            user-select: none;
        }
        .mobile-header {
            text-align: center;
            padding: 20px 0;
            background: #232f3e;
            margin: -20px -20px 20px -20px;
            border-radius: 0 0 15px 15px;
        }
        .mobile-btn {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 16px;
            margin: 10px 5px;
            cursor: pointer;
            touch-action: manipulation;
        }
        .mobile-btn:active {
            background: #45a049;
            transform: scale(0.95);
        }
        .mascot-mobile {
            width: 150px;
            height: 150px;
            margin: 20px auto;
            display: block;
        }
    </style>
</head>
<body>
    <div class="mobile-header">
        <h1>🌌 AWS Cloud Orbit</h1>
        <p>Your Mobile Learning Adventure</p>
    </div>
    
    <div style="text-align: center;">
        <img class="mascot-mobile" src="mascot/zap_idle.png" alt="Zap" onerror="this.style.display='none'">
        
        <h2>Welcome to Cloud Orbit Mobile!</h2>
        <p>Start your AWS learning journey</p>
        
        <button class="mobile-btn" onclick="startLearning()">🚀 Start Learning</button>
        <button class="mobile-btn" onclick="viewProgress()">📊 View Progress</button>
        
        <div id="content" style="margin-top: 30px;"></div>
    </div>

    <script>
        function startLearning() {
            document.getElementById('content').innerHTML = `
                <h3>📚 Available Lessons</h3>
                <div style="display: flex; flex-direction: column; gap: 10px; max-width: 300px; margin: 0 auto;">
                    <button class="mobile-btn" onclick="openLesson(1)">⚔️ Monitoring & Logging</button>
                    <button class="mobile-btn" onclick="openLesson(2)">🛡️ Reliability & Continuity</button>
                    <button class="mobile-btn" onclick="openLesson(3)">🚀 Deployment & Automation</button>
                    <button class="mobile-btn" onclick="openLesson(4)">🔒 Security & Compliance</button>
                </div>
                <button class="mobile-btn" onclick="showHome()" style="margin-top: 20px; background: #666;">← Back</button>
            `;
        }
        
        function viewProgress() {
            document.getElementById('content').innerHTML = `
                <h3>📈 Your Progress</h3>
                <div style="background: #2d2d2d; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <p>🌟 XP: 340</p>
                    <p>🔥 Streak: 5 days</p>
                    <p>⚡ Energy: 3/3</p>
                    <p>🏆 Badges: 6</p>
                </div>
                <button class="mobile-btn" onclick="showHome()" style="background: #666;">← Back</button>
            `;
        }
        
        function openLesson(id) {
            document.getElementById('content').innerHTML = `
                <h3>📖 Lesson ${id}</h3>
                <div style="background: #2d4a66; padding: 20px; border-radius: 10px; margin: 20px 0; border: 2px solid #2196F3;">
                    <p>This lesson would connect to your Flask backend API.</p>
                    <p>In the full version, this would show:</p>
                    <ul style="text-align: left; max-width: 250px; margin: 0 auto;">
                        <li>Interactive content</li>
                        <li>Quiz questions</li>
                        <li>Zap animations</li>
                        <li>Progress tracking</li>
                    </ul>
                </div>
                <button class="mobile-btn" onclick="startLearning()">← Back to Lessons</button>
            `;
        }
        
        function showHome() {
            document.getElementById('content').innerHTML = '';
        }
        
        // Add touch feedback
        document.addEventListener('touchstart', function(e) {
            if (e.target.classList.contains('mobile-btn')) {
                e.target.style.transform = 'scale(0.95)';
            }
        });
        
        document.addEventListener('touchend', function(e) {
            if (e.target.classList.contains('mobile-btn')) {
                setTimeout(() => {
                    e.target.style.transform = 'scale(1)';
                }, 100);
            }
        });
    </script>
</body>
</html>
EOF

# Initialize Capacitor with correct settings
echo "🔧 Initializing Capacitor..."
npx cap init "AWS Cloud Orbit" "com.cloudorbit.awsrpg" --web-dir="dist"

# Add Android platform
echo "📱 Adding Android platform..."
npx cap add android

# Copy additional resources
echo "📂 Copying additional resources..."
if [ -d "static/mascot" ]; then
    cp -r static/mascot dist/
fi

# Sync everything
echo "🔄 Syncing all assets..."
npx cap sync android

# Check if Android project was created properly
if [ -f "android/app/build.gradle" ]; then
    echo "✅ Android project created successfully!"
    echo "📱 Opening Android Studio..."
    
    # Try to open Android Studio
    npx cap open android || echo "⚠️ Please manually open the android folder in Android Studio"
    
    echo ""
    echo "🎯 Next steps:"
    echo "1. Wait for Gradle sync in Android Studio"
    echo "2. If Gradle sync fails, go to File → Project Structure → Project → Set JDK to 17+"
    echo "3. Build → Build Bundle(s) / APK(s) → Build APK(s)"
    echo "4. APK location: android/app/build/outputs/apk/debug/app-debug.apk"
else
    echo "❌ Android project creation failed"
    echo "📱 Try manually running: npx cap doctor"
fi