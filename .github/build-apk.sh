#!/bin/bash

# Build script for AWS Cloud Orbit APK

echo "🚀 Building AWS Cloud Orbit APK..."

# Create dist directory and copy static files
echo "📁 Preparing build directory..."
mkdir -p dist
cp -r static dist/
cp -r templates dist/

# Create a simple index.html that points to your Flask app
cat > dist/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS Cloud Orbit</title>
    <script>
        // Redirect to Flask app
        window.location.href = 'http://localhost:5001/';
    </script>
</head>
<body>
    <div style="text-align: center; margin-top: 50px; font-family: Arial;">
        <h2>Loading AWS Cloud Orbit...</h2>
        <p>Starting your AWS learning adventure!</p>
    </div>
</body>
</html>
EOF

# Initialize Capacitor if not already done
if [ ! -d "android" ]; then
    echo "🔧 Initializing Capacitor..."
    npx cap init
fi

# Add Android platform
echo "📱 Adding Android platform..."
npx cap add android

# Sync the web assets
echo "🔄 Syncing web assets..."
npx cap sync

# Open Android Studio
echo "📱 Opening Android Studio..."
npx cap open android

echo "✅ Build complete! Android Studio should be opening..."
echo "🎯 In Android Studio:"
echo "   1. Wait for Gradle sync to complete"
echo "   2. Click 'Build' > 'Build Bundle(s) / APK(s)' > 'Build APK(s)'"
echo "   3. APK will be in app/build/outputs/apk/debug/"