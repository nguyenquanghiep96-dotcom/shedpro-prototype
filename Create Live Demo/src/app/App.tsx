import { useState } from "react";
import MobileVersion1Default1 from "@/imports/MobileVersion1Default-1/index";
import MobileVersion1Color from "@/imports/MobileVersion1Color/index";
import MobileVersion1Exterior from "@/imports/MobileVersion1Exterior/index";
import MobileVersion1SidingColor from "@/imports/MobileVersion1SidingColor/index";
import MobileVersion1Door from "@/imports/MobileVersion1Door/index";

type Screen = "default" | "color" | "exterior" | "siding-color" | "door";

const SCREEN_W = 375;
const SCREEN_H = 812;

// Tab bar is inside ShedDetailsSection which starts at top-417, Navigation tabs are first (~44px)
const TAB_Y = 417;
const TAB_H = 44;

// Color siding choice row: after tabs (417+44) + Frame1 padding (16px)
const COLOR_CHOICE_Y = TAB_Y + TAB_H + 16; // 477
const COLOR_CHOICE_H = 44;

// Exterior Door card: same offset
const EXTERIOR_DOOR_Y = TAB_Y + TAB_H + 16; // 477
const EXTERIOR_DOOR_H = 50;

// SidingColor back nav: Tab panel at top-271, Frame1 h=54
const SIDING_BACK_Y = 271;
const SIDING_BACK_H = 54;
const SIDING_BACK_W = 220;

// Door back nav: Tab panel at top-159, Frame13 h=54
const DOOR_BACK_Y = 159;
const DOOR_BACK_H = 54;
const DOOR_BACK_W = 220;

function TabNavigationOverlay({ onNavigate }: { onNavigate: (s: Screen) => void }) {
  const handleClick = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    if (x < 68) onNavigate("default");
    else if (x < 128) onNavigate("default");
    else if (x < 210) onNavigate("color");
    else if (x < 300) onNavigate("exterior");
  };

  return (
    <div
      className="absolute cursor-pointer"
      style={{ top: TAB_Y, left: 0, width: SCREEN_W, height: TAB_H, zIndex: 20 }}
      onClick={handleClick}
    />
  );
}

export default function App() {
  const [screen, setScreen] = useState<Screen>("default");

  const screenLabel: Record<Screen, string> = {
    default: "Style",
    color: "Color",
    exterior: "Exterior",
    "siding-color": "Siding Color",
    door: "Door",
  };

  const hint: Record<Screen, string> = {
    default: "Tap the Color or Exterior tab to navigate",
    color: "Tap the Siding Color row · or switch tabs",
    exterior: "Tap the Door card to open door selection · or switch tabs",
    "siding-color": "Tap the back arrow (← Siding Color) to go back",
    door: "Tap the back arrow (← Door) to go back",
  };

  return (
    <div className="min-h-screen bg-[#e8e8e8] flex flex-col items-center justify-start py-6">
      {/* Label bar */}
      <div className="mb-3 flex gap-2 items-center">
        <span className="text-xs text-gray-500 font-sans tracking-wide uppercase">ShedPro Live Demo</span>
        <span className="text-xs bg-[#ff7048] text-white px-2.5 py-0.5 rounded-full font-sans font-semibold">
          {screenLabel[screen]}
        </span>
      </div>

      {/* Phone viewport */}
      <div
        className="relative overflow-y-auto shadow-2xl rounded-[44px]"
        style={{ width: SCREEN_W, height: SCREEN_H }}
      >
        {/* Screen content — tall enough for scrollable content */}
        <div className="absolute inset-x-0 top-0" style={{ width: SCREEN_W, height: 1500 }}>
          {screen === "default" && <MobileVersion1Default1 />}
          {screen === "color" && <MobileVersion1Color />}
          {screen === "exterior" && <MobileVersion1Exterior />}
          {screen === "siding-color" && <MobileVersion1SidingColor />}
          {screen === "door" && <MobileVersion1Door />}
        </div>

        {/* ── Click overlays for navigation ── */}

        {/* Main tab bar (Style, Size, Color, Exterior) */}
        {(screen === "default" || screen === "color" || screen === "exterior") && (
          <TabNavigationOverlay onNavigate={setScreen} />
        )}

        {/* Siding Color row → SidingColor screen */}
        {screen === "color" && (
          <div
            className="absolute cursor-pointer"
            style={{ top: COLOR_CHOICE_Y, left: 0, width: SCREEN_W, height: COLOR_CHOICE_H, zIndex: 20 }}
            onClick={() => setScreen("siding-color")}
          />
        )}

        {/* Door card → Door screen */}
        {screen === "exterior" && (
          <div
            className="absolute cursor-pointer"
            style={{ top: EXTERIOR_DOOR_Y, left: 0, width: SCREEN_W, height: EXTERIOR_DOOR_H, zIndex: 20 }}
            onClick={() => setScreen("door")}
          />
        )}

        {/* Back button SidingColor → Color */}
        {screen === "siding-color" && (
          <div
            className="absolute cursor-pointer"
            style={{ top: SIDING_BACK_Y, left: 0, width: SIDING_BACK_W, height: SIDING_BACK_H, zIndex: 20 }}
            onClick={() => setScreen("color")}
          />
        )}

        {/* Back button Door → Exterior */}
        {screen === "door" && (
          <div
            className="absolute cursor-pointer"
            style={{ top: DOOR_BACK_Y, left: 0, width: DOOR_BACK_W, height: DOOR_BACK_H, zIndex: 20 }}
            onClick={() => setScreen("exterior")}
          />
        )}
      </div>

      {/* Navigation hint */}
      <p className="mt-4 text-xs text-gray-400 font-sans text-center max-w-sm px-4">
        {hint[screen]}
      </p>
    </div>
  );
}
