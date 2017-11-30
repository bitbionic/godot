scons -c platform=android
scons -j6 platform=android tools=no target=Release
cd platform/android/java/
./gradlew build

