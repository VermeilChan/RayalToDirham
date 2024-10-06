[app]

# (str) Title of your application
title = Riyal to Dirham

# (str) Package name
package.name = riyaltodirham

# (str) Package domain (needed for android/ios packaging)
package.domain = me.misato

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse, or landscape-reverse
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
