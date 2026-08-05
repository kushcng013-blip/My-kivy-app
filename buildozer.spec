[app]

title = My Kivy App
package.name = mykivyapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf,mp3,wav

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

presplash.filename =
icon.filename =

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

log_level = 2

[buildozer]

warn_on_root = 1