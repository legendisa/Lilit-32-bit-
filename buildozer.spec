[app]
title = Lilit
package.name = lilit
package.domain = org.isa
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

# Android Ayarları
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Sadece 32-bit (Hatasız olması için tek mimari)
android.archs = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
