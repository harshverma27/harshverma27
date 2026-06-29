<!--
  harshverma27 · profile readme
  theme: cyber / neon · embedded systems + dev-tooling
  built to be diffable, just like nucleus configs.
-->

<a name="top"></a>

<!-- ============ HEADER ============ -->
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0d1117,40:0e4429,70:22d3ee,100:a78bfa&text=HARSH%20VERMA&fontColor=ffffff&fontSize=58&fontAlignY=36&desc=firmware%20%C2%B7%20developer%20tooling%20%C2%B7%20open%20source&descAlignY=58&descSize=18&animation=fadeIn" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=900&color=4ADE80&center=true&vCenter=true&width=720&height=46&lines=I+build+the+tools+I+wish+existed.;STM32+%2F%2F+Arduino+%2F%2F+Embedded+Linux;Rust+systems+%E2%80%A2+Python+%E2%80%A2+Kotlin;Open+source+%40+GNOME+%C2%B7+GIMP+%C2%B7+BABL)](https://git.io/typing-svg)

<br/>

[![Portfolio](https://img.shields.io/badge/heyharsh.me-0d1117?style=for-the-badge&logo=vercel&logoColor=4ade80&labelColor=0d1117)](https://heyharsh.me)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=22d3ee&labelColor=0d1117)](https://linkedin.com/in/harshhvermaa)
&nbsp;
[![Email](https://img.shields.io/badge/Email-0d1117?style=for-the-badge&logo=gmail&logoColor=f471b5&labelColor=0d1117)](mailto:harshkardam246@gmail.com)
&nbsp;
[![Profile Views](https://komarev.com/ghpvc/?username=harshverma27&style=for-the-badge&color=a78bfa&label=VISITORS&labelColor=0d1117)](https://github.com/harshverma27)

</div>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ ABOUT ============ -->
## <samp>$ whoami</samp>

```yaml
harsh@arch:~$ whoami --verbose
➜  EE undergrad @ NIT Hamirpur                 # '24 → '28
➜  I live one layer below the app             # firmware, CLIs, build tooling, CI
➜  Daily driver: Arch Linux                   # VS Code + a terminal that never closes
➜  Currently: turning STM32CubeIDE pain       # ...into a 4 MB Rust binary
```

<table>
<tr>
<td valign="top" width="50%">

**🛰️ &nbsp;What I'm into**
- Embedded systems & PCB / power design
- Developer tooling that's CLI-first & diffable
- CI/CD automation across GitHub & GitLab
- Real-time tracing, HALs, code-gen

</td>
<td valign="top" width="50%">

**⚡ &nbsp;Right now**
- Building **[Nucleus](https://github.com/harshverma27/nucleus)** — a modern STM32 platform in Rust
- Building **[SparkIDE](https://github.com/harshverma27/SparkIDE)** — block-based Arduino IDE
- Writing tests for **GIMP** & fixing **GNOME** CI

</td>
</tr>
</table>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ FLAGSHIP BUILDS ============ -->
## <samp>$ cat ./flagship_builds/*</samp>

### ◢ Nucleus &nbsp;·&nbsp; <sub>`a modern STM32 developer platform`</sub>

<table border="0">
<tr>
<td width="62%" valign="top">

> **Not an IDE replacement. A developer platform.**

STM32CubeIDE locks embedded devs into a 2 GB Eclipse fork, a click-through pin GUI, and opaque XML you can't diff or run in CI. **Nucleus** replaces both lock-ins with a **4 MB Rust CLI** and a VS Code extension:

- 🧩 &nbsp;Declarative `stm32.toml` — version-controllable, CI-friendly hardware config
- 🧮 &nbsp;**Pinmux compiler** + constraint solver instead of a point-and-click GUI
- 📡 &nbsp;**ITM trace daemon** — real-time debug without a \$600 Segger license
- 🦀 &nbsp;Rust core · TypeScript + React extension · LSP-powered editor UX

<a href="https://github.com/harshverma27/nucleus"><img src="https://img.shields.io/badge/Rust-0d1117?style=flat-square&logo=rust&logoColor=f74c00" /></a>
<a href="https://github.com/harshverma27/nucleus"><img src="https://img.shields.io/badge/STM32-0d1117?style=flat-square&logo=stmicroelectronics&logoColor=03234b" /></a>
<a href="https://github.com/harshverma27/nucleus"><img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=3178c6" /></a>
<br/>
<a href="https://github.com/harshverma27/nucleus"><img src="https://img.shields.io/badge/▶_explore_nucleus-0d1117?style=for-the-badge&labelColor=0e4429&color=0d1117" /></a>

</td>
<td width="40%" valign="top">

<a href="https://github.com/harshverma27/nucleus">
  <img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=harshverma27&repo=nucleus&hide_border=true&bg_color=0d1117&title_color=4ade80&icon_color=22d3ee&text_color=8b949e" />
</a>

<img src="https://img.shields.io/github/stars/harshverma27/nucleus?style=flat-square&logo=github&label=stars&color=4ade80&labelColor=0d1117" />
<img src="https://img.shields.io/github/last-commit/harshverma27/nucleus?style=flat-square&label=last&color=22d3ee&labelColor=0d1117" />
<img src="https://img.shields.io/github/languages/top/harshverma27/nucleus?style=flat-square&color=a78bfa&labelColor=0d1117" />

```toml
# stm32.toml — diffable hardware
[chip]
mcu = "STM32F411CEU6"

[pin.PA5]
mode  = "output"
label = "led"

[trace]
itm  = true   # real-time ITM
baud = 2_000_000
```

</td>
</tr>
</table>

### ◢ SparkIDE &nbsp;·&nbsp; <sub>`Arduino, without the cliff`</sub>

<table border="0">
<tr>
<td width="40%" valign="top">

<a href="https://github.com/harshverma27/SparkIDE">
  <img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=harshverma27&repo=SparkIDE&hide_border=true&bg_color=0d1117&title_color=4ade80&icon_color=22d3ee&text_color=8b949e" />
</a>

<img src="https://img.shields.io/github/stars/harshverma27/SparkIDE?style=flat-square&logo=github&label=stars&color=4ade80&labelColor=0d1117" />
<img src="https://img.shields.io/github/last-commit/harshverma27/SparkIDE?style=flat-square&label=last&color=22d3ee&labelColor=0d1117" />
<img src="https://img.shields.io/github/languages/top/harshverma27/SparkIDE?style=flat-square&color=a78bfa&labelColor=0d1117" />

```cpp
// snap blocks → get this C++
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(500);
}
```

</td>
<td width="62%" valign="top">

> **Scratch-like blocks → real Arduino C++ → flashed to your board, in one click.**

A lightweight, native **PyQt6** desktop IDE that wraps Google Blockly in a maker-lab shell so beginners on Linux can learn embedded the friendly way:

- 🧱 &nbsp;**50+ custom blocks** covering the full standard Arduino library
- 👁️ &nbsp;**Live C++ generation** — watch code write itself as you snap blocks
- 🔌 &nbsp;Board discovery, one-click compile **&** flash via `arduino-cli`
- 🟢 &nbsp;Offline Blockly via QtWebEngine · phosphor-green lab console UI

<a href="https://github.com/harshverma27/SparkIDE"><img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=ffd43b" /></a>
<a href="https://github.com/harshverma27/SparkIDE"><img src="https://img.shields.io/badge/PyQt6-0d1117?style=flat-square&logo=qt&logoColor=41cd52" /></a>
<a href="https://github.com/harshverma27/SparkIDE"><img src="https://img.shields.io/badge/Arduino-0d1117?style=flat-square&logo=arduino&logoColor=00979d" /></a>
<br/>
<a href="https://github.com/harshverma27/SparkIDE"><img src="https://img.shields.io/badge/▶_explore_sparkIDE-0d1117?style=for-the-badge&labelColor=0e4429&color=0d1117" /></a>

</td>
</tr>
</table>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ OPEN SOURCE ============ -->
## <samp>$ git log --author="harsh" --oneline</samp>

Active contributor to **GNOME** ([GitLab @harshverma](https://gitlab.gnome.org/harshverma)) — building the kind of unglamorous infra that keeps big projects honest.

| Project | Contribution | Impact |
| :-- | :-- | :-- |
| **GIMP** | Built a unit-testing framework from scratch for core libraries | Covered **65+ files**, wired into GitLab CI, surfaced a hidden env-var bug |
| **BABL · GEGL** | Fixed CI flaw spawning duplicate pipelines on every commit | Cut runner **resource usage by ~50%** |
| **GIMP** | Replaced weighted blur with Gaussian-distributed kernels | Sharper, spec-aligned blur strength |

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ ARSENAL ============ -->
## <samp>$ ls ./toolchain</samp>

<div align="center">

**Languages**

![Rust](https://img.shields.io/badge/Rust-0d1117?style=for-the-badge&logo=rust&logoColor=f74c00)
![C](https://img.shields.io/badge/C-0d1117?style=for-the-badge&logo=c&logoColor=a8b9cc)
![C++](https://img.shields.io/badge/C++-0d1117?style=for-the-badge&logo=cplusplus&logoColor=00599c)
![Python](https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=ffd43b)
![Kotlin](https://img.shields.io/badge/Kotlin-0d1117?style=for-the-badge&logo=kotlin&logoColor=7f52ff)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=for-the-badge&logo=gnubash&logoColor=4eaa25)
![SQL](https://img.shields.io/badge/SQL-0d1117?style=for-the-badge&logo=mysql&logoColor=4479a1)

**Embedded · Hardware**

![STM32](https://img.shields.io/badge/STM32-0d1117?style=for-the-badge&logo=stmicroelectronics&logoColor=03234b)
![Arduino](https://img.shields.io/badge/Arduino-0d1117?style=for-the-badge&logo=arduino&logoColor=00979d)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-0d1117?style=for-the-badge&logo=raspberrypi&logoColor=a22846)
![GTK](https://img.shields.io/badge/GTK+-0d1117?style=for-the-badge&logo=gtk&logoColor=7fe719)
![FFmpeg](https://img.shields.io/badge/FFmpeg-0d1117?style=for-the-badge&logo=ffmpeg&logoColor=007808)

**Backend · Mobile · Cloud**

![Django](https://img.shields.io/badge/Django-0d1117?style=for-the-badge&logo=django&logoColor=092e20)
![Jetpack Compose](https://img.shields.io/badge/Compose-0d1117?style=for-the-badge&logo=jetpackcompose&logoColor=4285f4)
![Firebase](https://img.shields.io/badge/Firebase-0d1117?style=for-the-badge&logo=firebase&logoColor=ffca28)
![PyQt](https://img.shields.io/badge/PyQt6-0d1117?style=for-the-badge&logo=qt&logoColor=41cd52)

**Automation · Systems**

![Linux](https://img.shields.io/badge/Linux-0d1117?style=for-the-badge&logo=linux&logoColor=fcc624)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0d1117?style=for-the-badge&logo=githubactions&logoColor=2088ff)
![GitLab CI](https://img.shields.io/badge/GitLab%20CI-0d1117?style=for-the-badge&logo=gitlab&logoColor=fc6d26)
![Git](https://img.shields.io/badge/Git-0d1117?style=for-the-badge&logo=git&logoColor=f05032)

</div>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ STATS ============ -->
## <samp>$ ./run --stats</samp>

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=harshverma27&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=4ade80&icon_color=22d3ee&text_color=8b949e&ring_color=a78bfa" />
&nbsp;
<img height="170" src="https://streak-stats.demolab.com?user=harshverma27&hide_border=true&background=0d1117&stroke=21262d&ring=22d3ee&fire=f471b5&currStreakLabel=4ade80&sideLabels=8b949e&dates=6e7681&currStreakNum=ffffff&sideNums=ffffff&dayLabels=4ade80&excludeDaysLabel=6e7681" />


</div>

<!-- snake eats the contribution graph (generated by .github/workflows/snake.yml) -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/harshverma27/harshverma27/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/harshverma27/harshverma27/output/snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/harshverma27/harshverma27/output/snake.svg" />
</picture>

</div>

<!-- full metrics card (generated by .github/workflows/metrics.yml) -->
<div align="center">

<img src="https://raw.githubusercontent.com/harshverma27/harshverma27/main/metrics.svg" alt="metrics" />

</div>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<!-- ============ FOOTER ============ -->
<div align="center">

> <samp>"The best way to predict the firmware is to flash it." — me, debugging at 3am</samp>

<a href="#top"><img src="https://img.shields.io/badge/▲_back_to_top-0d1117?style=for-the-badge&labelColor=0e4429&color=0d1117" /></a>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=120&color=0:a78bfa,30:22d3ee,60:0e4429,100:0d1117&animation=fadeIn" />

</div>
