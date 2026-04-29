"""
Clientnest Design System - Lusion.co Inspired
============================================

A comprehensive design system featuring glassmorphism, ambient effects,
and premium typography for a cohesive, modern user experience.

Color Palette:
- void: #030305 (deep black background)
- nestAccent: #6366f1 (primary indigo)
- nestGlow: #8b5cf6 (secondary purple)
- nestSurface: rgba(15, 15, 20, 0.6) (glass surface)

Typography:
- Display: Space Grotesk (headings, large text)
- Sans: Inter (body text, UI elements)
- Mono: JetBrains Mono (code, technical text, small labels)
"""

import reflex as rx

# ============================================================================
# COLOR PALETTE
# ============================================================================

class Colors:
    """Lusion.co-inspired color palette"""
    
    # Primary colors
    VOID = "#030305"
    NEST_ACCENT = "#6366f1"
    NEST_GLOW = "#8b5cf6"
    NEST_SURFACE = "rgba(15, 15, 20, 0.6)"
    
    # Semantic colors
    SUCCESS = "#10b981"
    WARNING = "#f59e0b"
    ERROR = "#ef4444"
    INFO = "#3b82f6"
    
    # Text colors
    TEXT_PRIMARY = "#f8fafc"
    TEXT_SECONDARY = "#94a3b8"
    TEXT_TERTIARY = "#64748b"
    TEXT_MUTED = "#475569"
    
    # Border colors
    BORDER_LIGHT = "rgba(255, 255, 255, 0.1)"
    BORDER_MEDIUM = "rgba(255, 255, 255, 0.15)"
    BORDER_DARK = "rgba(255, 255, 255, 0.05)"
    
    # Background colors
    BG_DARK = "#0a0a0f"
    BG_CARD = "rgba(15, 15, 20, 0.8)"
    BG_HOVER = "rgba(99, 102, 241, 0.1)"
    
    # Gradient colors
    GRADIENT_PRIMARY = "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)"
    GRADIENT_TEXT = "linear-gradient(135deg, #ffffff 0%, #a5b4fc 50%, #818cf8 100%)"


# ============================================================================
# TYPOGRAPHY
# ============================================================================

class Typography:
    """Typography system with custom fonts"""
    
    # Font families
    DISPLAY = "Space Grotesk, sans-serif"
    SANS = "Inter, sans-serif"
    MONO = "JetBrains Mono, monospace"
    
    # Font sizes
    TEXT_XS = "0.75rem"      # 12px
    TEXT_SM = "0.875rem"     # 14px
    TEXT_BASE = "1rem"       # 16px
    TEXT_LG = "1.125rem"     # 18px
    TEXT_XL = "1.25rem"      # 20px
    TEXT_2XL = "1.5rem"      # 24px
    TEXT_3XL = "1.875rem"    # 30px
    TEXT_4XL = "2.25rem"     # 36px
    TEXT_5XL = "3rem"        # 48px
    TEXT_6XL = "3.75rem"     # 60px
    TEXT_7XL = "4.5rem"      # 72px
    
    # Font weights
    FONT_LIGHT = "300"
    FONT_NORMAL = "400"
    FONT_MEDIUM = "500"
    FONT_SEMIBOLD = "600"
    FONT_BOLD = "700"
    
    # Line heights
    LEADING_TIGHT = "1.25"
    LEADING_NORMAL = "1.5"
    LEADING_RELAXED = "1.75"
    LEADING_LOOSE = "2"
    
    # Letter spacing
    TRACKING_TIGHT = "-0.025em"
    TRACKING_NORMAL = "0"
    TRACKING_WIDE = "0.025em"
    TRACKING_WIDER = "0.05em"
    TRACKING_WIDEST = "0.1em"


# ============================================================================
# SPACING
# ============================================================================

class Spacing:
    """Consistent spacing scale"""
    
    SPACE_0 = "0"
    SPACE_1 = "0.25rem"      # 4px
    SPACE_2 = "0.5rem"       # 8px
    SPACE_3 = "0.75rem"      # 12px
    SPACE_4 = "1rem"         # 16px
    SPACE_5 = "1.25rem"      # 20px
    SPACE_6 = "1.5rem"       # 24px
    SPACE_8 = "2rem"         # 32px
    SPACE_10 = "2.5rem"      # 40px
    SPACE_12 = "3rem"        # 48px
    SPACE_16 = "4rem"        # 64px
    SPACE_20 = "5rem"        # 80px
    SPACE_24 = "6rem"        # 96px
    
    # Gap sizes
    GAP_XS = "0.5rem"
    GAP_SM = "1rem"
    GAP_MD = "1.5rem"
    GAP_LG = "2rem"
    GAP_XL = "3rem"


# ============================================================================
# BORDER RADIUS
# ============================================================================

class BorderRadius:
    """Consistent border radius scale"""
    
    RADIUS_NONE = "0"
    RADIUS_SM = "0.25rem"    # 4px
    RADIUS_MD = "0.5rem"     # 8px
    RADIUS_LG = "0.75rem"    # 12px
    RADIUS_XL = "1rem"       # 16px
    RADIUS_2XL = "1.5rem"    # 24px
    RADIUS_3XL = "2rem"       # 32px
    RADIUS_FULL = "9999px"


# ============================================================================
# SHADOWS
# ============================================================================

class Shadows:
    """Enhanced shadow system for depth"""
    
    SHADOW_SM = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    SHADOW_MD = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
    SHADOW_LG = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
    SHADOW_XL = "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
    SHADOW_2XL = "0 25px 50px -12px rgba(0, 0, 0, 0.25)"
    
    # Glassmorphism shadows
    SHADOW_GLASS = "0 25px 50px -12px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1)"
    SHADOW_GLASS_HOVER = "0 30px 60px -15px rgba(0, 0, 0, 0.8), 0 0 30px rgba(99, 102, 241, 0.1)"
    
    # Glow effects
    GLOW_ACCENT = "0 0 20px rgba(99, 102, 241, 0.3)"
    GLOW_SUCCESS = "0 0 20px rgba(16, 185, 129, 0.3)"
    GLOW_ERROR = "0 0 20px rgba(239, 68, 68, 0.3)"


# ============================================================================
# TRANSITIONS
# ============================================================================

class Transitions:
    """Smooth transition utilities"""
    
    DURATION_FAST = "150ms"
    DURATION_NORMAL = "300ms"
    DURATION_SLOW = "500ms"
    DURATION_SLOWER = "700ms"
    
    EASING_DEFAULT = "cubic-bezier(0.4, 0, 0.2, 1)"
    EASING_IN = "cubic-bezier(0.4, 0, 1, 1)"
    EASING_OUT = "cubic-bezier(0, 0, 0.2, 1)"
    EASING_IN_OUT = "cubic-bezier(0.4, 0, 0.2, 1)"
    EASING_BOUNCE = "cubic-bezier(0.68, -0.55, 0.265, 1.55)"
    
    # Transition combinations
    TRANSITION_FAST = f"all {DURATION_FAST} {EASING_DEFAULT}"
    TRANSITION_NORMAL = f"all {DURATION_NORMAL} {EASING_DEFAULT}"
    TRANSITION_SLOW = f"all {DURATION_SLOW} {EASING_DEFAULT}"
    TRANSITION_SMOOTH = f"all {DURATION_SLOW} cubic-bezier(0.16, 1, 0.3, 1)"


# ============================================================================
# GLASSMORPHISM UTILITIES
# ============================================================================

class Glassmorphism:
    """Glassmorphism component styles"""
    
    # Base glass panel
    GLASS_PANEL = {
        "background": Colors.NEST_SURFACE,
        "backdrop_filter": "blur(24px)",
        "webkit_backdrop_filter": "blur(24px)",
        "border": f"1px solid {Colors.BORDER_LIGHT}",
        "box_shadow": Shadows.SHADOW_GLASS,
        "transition": Transitions.TRANSITION_SMOOTH,
    }
    
    # Glass panel hover state
    GLASS_PANEL_HOVER = {
        "border_color": "rgba(99, 102, 241, 0.3)",
        "transform": "translateY(-5px)",
        "box_shadow": Shadows.SHADOW_GLASS_HOVER,
    }
    
    # Glass button
    GLASS_BUTTON = {
        "background": "rgba(99, 102, 241, 0.1)",
        "backdrop_filter": "blur(12px)",
        "webkit_backdrop_filter": "blur(12px)",
        "border": f"1px solid {Colors.BORDER_MEDIUM}",
        "transition": Transitions.TRANSITION_NORMAL,
    }
    
    # Glass input
    GLASS_INPUT = {
        "background": "rgba(0, 0, 0, 0.3)",
        "backdrop_filter": "blur(8px)",
        "webkit_backdrop_filter": "blur(8px)",
        "border": f"1px solid {Colors.BORDER_DARK}",
        "transition": Transitions.TRANSITION_FAST,
    }
    
    # Glass card
    GLASS_CARD = {
        "background": Colors.BG_CARD,
        "backdrop_filter": "blur(16px)",
        "webkit_backdrop_filter": "blur(16px)",
        "border": f"1px solid {Colors.BORDER_LIGHT}",
        "box_shadow": Shadows.SHADOW_LG,
        "transition": Transitions.TRANSITION_SMOOTH,
    }


# ============================================================================
# ANIMATION UTILITIES
# ============================================================================

class Animations:
    """Animation utilities for dynamic effects"""
    
    # Float animations
    FLOAT_SLOW = "float 20s ease-in-out infinite"
    FLOAT_DELAYED = "float 25s ease-in-out infinite 5s"
    
    # Pulse animations
    PULSE_GLOW = "pulseGlow 4s cubic-bezier(0.4, 0, 0.6, 1) infinite"
    PULSE_SUBTLE = "pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite"
    
    # Fade animations
    FADE_IN = "fadeIn 0.5s ease-out"
    FADE_OUT = "fadeOut 0.5s ease-out"
    FADE_UP = "fadeUp 0.6s ease-out"
    
    # Slide animations
    SLIDE_IN_RIGHT = "slideInRight 0.5s ease-out"
    SLIDE_IN_LEFT = "slideInLeft 0.5s ease-out"
    
    # Scale animations
    SCALE_IN = "scaleIn 0.3s ease-out"
    SCALE_UP = "scaleUp 0.2s ease-out"
    
    # Gradient animations
    GRADIENT_SHIFT = "gradient-shift 8s linear infinite"


# ============================================================================
# RESPONSIVE BREAKPOINTS
# ============================================================================

class Breakpoints:
    """Responsive design breakpoints"""
    
    SM = "640px"      # Small screens
    MD = "768px"      # Medium screens (tablets)
    LG = "1024px"     # Large screens (laptops)
    XL = "1280px"     # Extra large screens (desktops)
    XXL = "1536px"    # 2X large screens


# ============================================================================
# Z-INDEX SCALE
# ============================================================================

class ZIndex:
    """Consistent z-index scale"""
    
    DROPDOWN = 1000
    STICKY = 1020
    FIXED = 1030
    MODAL_BACKDROP = 1040
    MODAL = 1050
    POPOVER = 1060
    TOOLTIP = 1070
    MAXIMUM = 9999


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_glass_style(hover: bool = False) -> dict:
    """Get glassmorphism style with optional hover state"""
    base = Glassmorphism.GLASS_PANEL.copy()
    if hover:
        base.update(Glassmorphism.GLASS_PANEL_HOVER)
    return base


def get_text_gradient() -> str:
    """Get gradient text style"""
    return f"""
        background: {Colors.GRADIENT_TEXT};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: {Animations.GRADIENT_SHIFT};
    """


def get_glow_color(color: str = Colors.NEST_ACCENT) -> str:
    """Get glow effect for a specific color"""
    return f"0 0 20px {color}40"  # 40 = 25% opacity


def get_transition(
    duration: str = Transitions.DURATION_NORMAL,
    easing: str = Transitions.EASING_DEFAULT,
    properties: str = "all"
) -> str:
    """Get custom transition string"""
    return f"{properties} {duration} {easing}"


# ============================================================================
# THEME CONFIGURATION
# ============================================================================

class ThemeConfig:
    """Complete theme configuration for Reflex"""
    
    @staticmethod
    def get_config() -> dict:
        """Get complete theme configuration"""
        return {
            "colors": {
                "void": Colors.VOID,
                "nestAccent": Colors.NEST_ACCENT,
                "nestGlow": Colors.NEST_GLOW,
                "nestSurface": Colors.NEST_SURFACE,
                "textPrimary": Colors.TEXT_PRIMARY,
                "textSecondary": Colors.TEXT_SECONDARY,
                "textTertiary": Colors.TEXT_TERTIARY,
                "borderLight": Colors.BORDER_LIGHT,
                "borderMedium": Colors.BORDER_MEDIUM,
                "borderDark": Colors.BORDER_DARK,
                "bgDark": Colors.BG_DARK,
                "bgCard": Colors.BG_CARD,
                "bgHover": Colors.BG_HOVER,
            },
            "fonts": {
                "display": Typography.DISPLAY,
                "sans": Typography.SANS,
                "mono": Typography.MONO,
            },
            "font_sizes": {
                "xs": Typography.TEXT_XS,
                "sm": Typography.TEXT_SM,
                "base": Typography.TEXT_BASE,
                "lg": Typography.TEXT_LG,
                "xl": Typography.TEXT_XL,
                "2xl": Typography.TEXT_2XL,
                "3xl": Typography.TEXT_3XL,
                "4xl": Typography.TEXT_4XL,
                "5xl": Typography.TEXT_5XL,
                "6xl": Typography.TEXT_6XL,
                "7xl": Typography.TEXT_7XL,
            },
            "shadows": {
                "sm": Shadows.SHADOW_SM,
                "md": Shadows.SHADOW_MD,
                "lg": Shadows.SHADOW_LG,
                "xl": Shadows.SHADOW_XL,
                "2xl": Shadows.SHADOW_2XL,
                "glass": Shadows.SHADOW_GLASS,
                "glassHover": Shadows.SHADOW_GLASS_HOVER,
                "glowAccent": Shadows.GLOW_ACCENT,
                "glowSuccess": Shadows.GLOW_SUCCESS,
                "glowError": Shadows.GLOW_ERROR,
            },
            "border_radius": {
                "none": BorderRadius.RADIUS_NONE,
                "sm": BorderRadius.RADIUS_SM,
                "md": BorderRadius.RADIUS_MD,
                "lg": BorderRadius.RADIUS_LG,
                "xl": BorderRadius.RADIUS_XL,
                "2xl": BorderRadius.RADIUS_2XL,
                "3xl": BorderRadius.RADIUS_3XL,
                "full": BorderRadius.RADIUS_FULL,
            },
            "transitions": {
                "fast": Transitions.TRANSITION_FAST,
                "normal": Transitions.TRANSITION_NORMAL,
                "slow": Transitions.TRANSITION_SLOW,
                "smooth": Transitions.TRANSITION_SMOOTH,
            },
        }


# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    "Colors",
    "Typography",
    "Spacing",
    "BorderRadius",
    "Shadows",
    "Transitions",
    "Glassmorphism",
    "Animations",
    "Breakpoints",
    "ZIndex",
    "ThemeConfig",
    "get_glass_style",
    "get_text_gradient",
    "get_glow_color",
    "get_transition",
]