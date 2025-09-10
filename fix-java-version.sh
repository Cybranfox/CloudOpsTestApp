#!/bin/bash

# Fix Java Version for Android Build

echo "🔧 Fixing Java version compatibility..."

# Check current Java version
echo "Current Java version:"
java -version

echo ""
echo "Current JAVA_HOME: $JAVA_HOME"

# Kill all gradle processes
echo "🛑 Stopping Gradle processes..."
pkill -f gradle 2>/dev/null || true
pkill -f "Android Studio" 2>/dev/null || true

# Clear Gradle cache
echo "🧹 Clearing Gradle cache..."
rm -rf ~/.gradle/caches/ 2>/dev/null || true
rm -rf ~/.gradle/daemon/ 2>/dev/null || true

# Remove and recreate android project with correct settings
echo "🔄 Recreating Android project..."
cd /c/Users/Manny/Documents/cloudopstestapp/AWS_Orbit_RPG
rm -rf android

# Create gradle.properties to force Java 17
cat > gradle.properties << 'EOF'
org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m
org.gradle.parallel=true
org.gradle.daemon=true
org.gradle.configureondemand=true
android.useAndroidX=true
android.enableJetifier=true
org.gradle.java.home=C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.8.101-hotspot
EOF

# Update capacitor config to be more compatible
cat > capacitor.config.json << 'EOF'
{
  "appId": "com.cloudorbit.awsrpg",
  "appName": "AWS Cloud Orbit",
  "webDir": "dist",
  "plugins": {
    "SplashScreen": {
      "launchShowDuration": 2000,
      "backgroundColor": "#232f3e",
      "showSpinner": false
    }
  },
  "android": {
    "buildOptions": {
      "keystorePath": "",
      "keystorePassword": "",
      "keystoreAlias": "",
      "keystoreAliasPassword": "",
      "releaseType": "APK"
    }
  }
}
EOF

# Recreate Android project
echo "📱 Adding Android platform..."
npx cap add android

# Copy gradle.properties to android folder
cp gradle.properties android/

# Update Android gradle files for better compatibility
echo "🔧 Updating Android build files..."

# Update android/build.gradle
cat > android/build.gradle << 'EOF'
// Top-level build file where you can add configuration options common to all sub-projects/modules.

buildscript {

    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.0.2'
        classpath 'com.google.gms:google-services:4.3.15'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

apply from: "variables.gradle"

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
EOF

# Sync the project
echo "🔄 Syncing Capacitor..."
npx cap sync

echo ""
echo "✅ Android project recreated with Java compatibility fixes!"
echo ""
echo "🎯 Next steps:"
echo "1. Open Android Studio"
echo "2. Go to File → Project Structure → Project"
echo "3. Set Project SDK to JDK 17 (not 21)"
echo "4. Click Apply and OK"
echo "5. Wait for Gradle sync to complete"
echo "6. Build → Build Bundle(s) / APK(s) → Build APK(s)"
echo ""
echo "📱 If you still get errors, try:"
echo "   File → Invalidate Caches and Restart"