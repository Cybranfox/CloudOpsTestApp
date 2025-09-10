#!/bin/bash

# Simple APK Build for AWS Cloud Orbit (No Capacitor needed)

echo "🚀 Simple APK Build for AWS Cloud Orbit..."

# Check if we have Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first:"
    echo "   Download from: https://nodejs.org/"
    echo "   Or run: winget install OpenJS.NodeJS"
    exit 1
fi

# Check if we have npm
if ! command -v npm &> /dev/null; then
    echo "❌ NPM not found. Please install Node.js with NPM"
    exit 1
fi

echo "✅ Node.js $(node --version) found"
echo "✅ NPM $(npm --version) found"

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    echo "📦 Creating package.json..."
    cat > package.json << 'EOF'
{
  "name": "aws-cloud-orbit",
  "version": "1.0.0",
  "description": "AWS Learning RPG Game",
  "main": "app.py",
  "scripts": {
    "build": "npx cap sync",
    "android": "npx cap open android"
  },
  "dependencies": {
    "@capacitor/core": "^5.0.0",
    "@capacitor/android": "^5.0.0",
    "@capacitor/cli": "^5.0.0"
  }
}
EOF
fi

# Install dependencies
echo "📦 Installing Capacitor dependencies..."
npm install

# Initialize Capacitor
echo "🔧 Initializing Capacitor..."
npx cap init "AWS Cloud Orbit" "com.cloudorbit.awsrpg" --web-dir=dist

# Create dist directory and copy files
echo "📁 Preparing build directory..."
mkdir -p dist
cp -r static dist/ 2>/dev/null || echo "No static folder found"
cp -r templates dist/ 2>/dev/null || echo "No templates folder found"

# Create index.html for mobile
cat > dist/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS Cloud Orbit</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #1a1a1a;
            color: white;
            text-align: center;
            padding: 50px 20px;
        }
        .logo {
            font-size: 2em;
            margin-bottom: 20px;
        }
        .loading {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        .btn {
            background: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 1.2em;
            margin: 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="logo">🌌 AWS Cloud Orbit</div>
    <div class="loading">Starting your AWS learning adventure...</div>
    
    <script>
        // In a real mobile app, this would connect to your Flask backend
        // For now, show a simple interface
        setTimeout(() => {
            document.body.innerHTML = `
                <div class="logo">🌌 AWS Cloud Orbit</div>
                <h2>Welcome to your AWS Learning Adventure!</h2>
                <p>This is the mobile app version.</p>
                <button class="btn" onclick="startLearning()">🚀 Start Learning</button>
                <div id="content" style="margin-top: 30px;"></div>
            `;
        }, 2000);
        
        function startLearning() {
            document.getElementById('content').innerHTML = `
                <h3>📚 Available Lessons:</h3>
                <button class="btn" onclick="showLesson(1)">Lesson 1: Monitoring & Logging</button>
                <button class="btn" onclick="showLesson(2)">Lesson 2: Reliability</button>
                <button class="btn" onclick="showLesson(3)">Lesson 3: Deployment</button>
            `;
        }
        
        function showLesson(id) {
            document.getElementById('content').innerHTML = `
                <h3>🎯 Lesson ${id}</h3>
                <p>This lesson would connect to your Flask backend API.</p>
                <button class="btn" onclick="startLearning()">← Back to Lessons</button>
            `;
        }
    </script>
</body>
</html>
EOF

# Add Android platform
echo "📱 Adding Android platform..."
npx cap add android

# Sync files
echo "🔄 Syncing web assets..."
npx cap sync

# Try to open Android Studio
echo "📱 Opening Android Studio..."
if command -v "android-studio" &> /dev/null; then
    npx cap open android
elif [ -f "/opt/android-studio/bin/studio.sh" ]; then
    /opt/android-studio/bin/studio.sh android/
else
    echo "⚠️ Android Studio not found in PATH"
    echo "📂 Android project created in: ./android/"
    echo "🎯 Manually open this folder in Android Studio to build APK"
fi

echo ""
echo "✅ APK build setup complete!"
echo ""
echo "🎯 Next steps in Android Studio:"
echo "   1. Wait for Gradle sync to complete (this may take a few minutes)"
echo "   2. Click Build → Build Bundle(s) / APK(s) → Build APK(s)"
echo "   3. APK will be created in: android/app/build/outputs/apk/debug/"
echo ""
echo "📱 Your APK will be ready for testing on your phone!"