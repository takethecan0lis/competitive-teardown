# iPhone Mirroring playbook

Drive an iPhone app from the user's Mac through Apple's iPhone Mirroring app, using computer use. Confirm each step on your setup.

## Setup checklist for the user
1. Mac on macOS Sequoia or later; iPhone on iOS 18 or later; both signed in to the same Apple Account with two-factor authentication.
2. iPhone locked, nearby, and charged; Bluetooth and Wi-Fi on for both.
3. Open the iPhone Mirroring app on the Mac and complete its one-time setup.
4. In the Claude desktop app, approve computer-use access for iPhone Mirroring when asked.
5. Open the target app on the mirrored phone and leave it on the home screen of the app.
6. Turn on a Focus mode so other apps' notifications do not appear.

## Access
- Request access to "iPhone Mirroring" (bundle id `com.apple.ScreenContinuity`). It is granted at full tier.
- Prefer background app tools (`app_screenshot`, `app_click`, `app_key`, `app_zoom`) so the user keeps their screen.

## Driving rules that held up
- **Taps:** background clicks work. Click the center of a control.
- **Scrolling:** drag and scroll gestures do not work through mirroring. Use the keyboard: Page Down and Page Up scroll the frontmost scroll view.
- **Typing:** background typing does not register in iOS text fields. Use suggestion chips when the app offers them; otherwise hand typing to the user.
- **Dismissing sheets:** tap the dimmed background above the sheet. Do not tap a sheet's X when its purpose is unclear; closing a picker with X can change a saved setting.
- **Small controls:** zoom on the region first to find exact positions of small X buttons and icons.
- **Bottom edge:** avoid taps near the bottom edge; they can trigger the iOS home gesture and leave the app.
- **Back navigation:** use the app's back arrow at top left; swiping is unavailable.

## Recovery
- When the user picks up the phone, mirroring pauses and shows a Resume or Connect screen. Wait until the user puts the phone down, then click the Resume button. Re-screenshot before continuing.
- If the app relaunches or logs out, stop and ask the user.
- If a tap lands on something unintended, stop, record it, and reverse it immediately (back out, choose Discard, or undo). Tell the user what happened.

## Evidence
- Screenshot each new screen once; describe it in session notes rather than storing many images.
- Record the app version and build from the settings or about screen.
