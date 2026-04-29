"""
Glassmorphism Components
========================

Premium glass-effect components for the Clientnest dashboard.
These components provide the lusion.co-inspired aesthetic with
blur effects, transparency, and smooth animations.

Components:
- glass_panel: Base glass container
- glass_card: Glass card with hover effects
- glass_button: Glass-styled buttons
- glass_input: Glass-styled form inputs
- glass_badge: Small glass badges
- glass_divider: Glass-styled dividers
"""

import reflex as rx
from ..styles import (
    Colors,
    Glassmorphism,
    BorderRadius,
    Shadows,
    Transitions,
    Typography,
    Spacing,
)


# ============================================================================
# BASE GLASS PANEL
# ============================================================================

def glass_panel(
    *children,
    **props
) -> rx.Component:
    """
    Base glass panel component with blur and transparency effects.
    
    Args:
        *children: Child components
        **props: Additional props (hover, padding, etc.)
    
    Returns:
        Glass panel component
    """
    hover = props.pop("hover", False)
    padding = props.pop("padding", "6")
    border_radius = props.pop("border_radius", BorderRadius.RADIUS_2XL)
    
    base_style = {
        "background": Colors.NEST_SURFACE,
        "backdrop_filter": "blur(24px)",
        "webkit_backdrop_filter": "blur(24px)",
        "border": f"1px solid {Colors.BORDER_LIGHT}",
        "box_shadow": Shadows.SHADOW_GLASS,
        "transition": Transitions.TRANSITION_SMOOTH,
    }
    
    if hover:
        base_style.update({
            "_hover": {
                "border_color": "rgba(99, 102, 241, 0.3)",
                "transform": "translateY(-5px)",
                "box_shadow": Shadows.SHADOW_GLASS_HOVER,
            }
        })
    
    return rx.box(
        *children,
        padding=padding,
        border_radius=border_radius,
        style=base_style,
        **props
    )


# ============================================================================
# GLASS CARD
# ============================================================================

def glass_card(
    *children,
    **props
) -> rx.Component:
    """
    Glass card component with enhanced hover effects.
    
    Args:
        *children: Child components
        **props: Additional props
    
    Returns:
        Glass card component
    """
    padding = props.pop("padding", "8")
    border_radius = props.pop("border_radius", BorderRadius.RADIUS_3XL)
    
    return rx.box(
        *children,
        padding=padding,
        border_radius=border_radius,
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        box_shadow=Shadows.SHADOW_LG,
        transition=Transitions.TRANSITION_SMOOTH,
        _hover={
            "border_color": "rgba(99, 102, 241, 0.3)",
            "transform": "translateY(-5px)",
            "box_shadow": Shadows.SHADOW_GLASS_HOVER,
        },
        **props
    )


# ============================================================================
# GLASS BUTTON
# ============================================================================

def glass_button(
    text: str,
    **props
) -> rx.Component:
    """
    Glass-styled button with hover effects.
    
    Args:
        text: Button text
        **props: Additional props (variant, size, on_click, etc.)
    
    Returns:
        Glass button component
    """
    variant = props.pop("variant", "primary")
    size = props.pop("size", "md")
    on_click = props.pop("on_click", None)
    
    # Size configurations
    sizes = {
        "sm": {"padding": f"{"2"} {"4"}", "font_size": Typography.TEXT_SM},
        "md": {"padding": f"{"3"} {"6"}", "font_size": Typography.TEXT_BASE},
        "lg": {"padding": f"{"4"} {"8"}", "font_size": Typography.TEXT_LG},
    }
    
    # Variant configurations
    variants = {
        "primary": {
            "background": Colors.NEST_ACCENT,
            "color": Colors.TEXT_PRIMARY,
            "border": "none",
            "_hover": {
                "background": Colors.NEST_GLOW,
                "transform": "scale(1.05)",
                "box_shadow": Shadows.GLOW_ACCENT,
            }
        },
        "secondary": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.TEXT_PRIMARY,
            "border": f"1px solid {Colors.BORDER_MEDIUM}",
            "_hover": {
                "background": "rgba(99, 102, 241, 0.2)",
                "border_color": Colors.NEST_ACCENT,
            }
        },
        "ghost": {
            "background": "transparent",
            "color": Colors.TEXT_SECONDARY,
            "border": f"1px solid {Colors.BORDER_DARK}",
            "_hover": {
                "background": Colors.BG_HOVER,
                "color": Colors.TEXT_PRIMARY,
                "border_color": Colors.BORDER_MEDIUM,
            }
        },
    }
    
    size_config = sizes.get(size, sizes["md"])
    variant_config = variants.get(variant, variants["primary"])
    
    return rx.button(
        text,
        padding=size_config["padding"],
        font_size=size_config["font_size"],
        font_family=Typography.SANS,
        font_weight=Typography.FONT_MEDIUM,
        border_radius=BorderRadius.RADIUS_FULL,
        cursor="pointer",
        transition=Transitions.TRANSITION_NORMAL,
        on_click=on_click,
        **variant_config,
        **props
    )


# ============================================================================
# GLASS INPUT
# ============================================================================

def glass_input(
    placeholder: str,
    **props
) -> rx.Component:
    """
    Glass-styled input field.
    
    Args:
        placeholder: Input placeholder text
        **props: Additional props (type, value, on_change, etc.)
    
    Returns:
        Glass input component
    """
    input_type = props.pop("type", "text")
    value = props.pop("value", "")
    on_change = props.pop("on_change", None)
    required = props.pop("required", False)
    
    return rx.input(
        placeholder=placeholder,
        type=input_type,
        value=value,
        on_change=on_change,
        required=required,
        background="rgba(0, 0, 0, 0.3)",
        backdrop_filter="blur(8px)",
        webkit_backdrop_filter="blur(8px)",
        border=f"1px solid {Colors.BORDER_DARK}",
        border_radius=BorderRadius.RADIUS_LG,
        padding=f"{"3"} {"4"}",
        color=Colors.TEXT_PRIMARY,
        font_family=Typography.SANS,
        font_size=Typography.TEXT_BASE,
        transition=Transitions.TRANSITION_FAST,
        _focus={
            "border_color": Colors.NEST_ACCENT,
            "box_shadow": Shadows.GLOW_ACCENT,
            "outline": "none",
        },
        _placeholder={
            "color": Colors.TEXT_TERTIARY,
        },
        **props
    )


# ============================================================================
# GLASS TEXTAREA
# ============================================================================

def glass_textarea(
    placeholder: str,
    **props
) -> rx.Component:
    """
    Glass-styled textarea field.
    
    Args:
        placeholder: Textarea placeholder text
        **props: Additional props (value, on_change, rows, etc.)
    
    Returns:
        Glass textarea component
    """
    value = props.pop("value", "")
    on_change = props.pop("on_change", None)
    rows = str(props.pop("rows", 4))
    
    return rx.text_area(
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        rows=rows,
        background="rgba(0, 0, 0, 0.3)",
        backdrop_filter="blur(8px)",
        webkit_backdrop_filter="blur(8px)",
        border=f"1px solid {Colors.BORDER_DARK}",
        border_radius=BorderRadius.RADIUS_LG,
        padding=f"{"3"} {"4"}",
        color=Colors.TEXT_PRIMARY,
        font_family=Typography.SANS,
        font_size=Typography.TEXT_BASE,
        transition=Transitions.TRANSITION_FAST,
        _focus={
            "border_color": Colors.NEST_ACCENT,
            "box_shadow": Shadows.GLOW_ACCENT,
            "outline": "none",
        },
        _placeholder={
            "color": Colors.TEXT_TERTIARY,
        },
        **props
    )


# ============================================================================
# GLASS BADGE
# ============================================================================

def glass_badge(
    text: str,
    **props
) -> rx.Component:
    """
    Glass-styled badge component.
    
    Args:
        text: Badge text
        **props: Additional props (variant, size, etc.)
    
    Returns:
        Glass badge component
    """
    variant = props.pop("variant", "default")
    size = props.pop("size", "sm")
    
    # Size configurations
    sizes = {
        "xs": {"padding": f"{"1"} {"2"}", "font_size": Typography.TEXT_XS},
        "sm": {"padding": f"{"1"} {"3"}", "font_size": Typography.TEXT_SM},
        "md": {"padding": f"{"2"} {"4"}", "font_size": Typography.TEXT_BASE},
    }
    
    # Variant configurations
    variants = {
        "default": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.NEST_ACCENT,
            "border": f"1px solid rgba(99, 102, 241, 0.2)",
        },
        "success": {
            "background": "rgba(16, 185, 129, 0.1)",
            "color": Colors.SUCCESS,
            "border": f"1px solid rgba(16, 185, 129, 0.2)",
        },
        "warning": {
            "background": "rgba(245, 158, 11, 0.1)",
            "color": Colors.WARNING,
            "border": f"1px solid rgba(245, 158, 11, 0.2)",
        },
        "error": {
            "background": "rgba(239, 68, 68, 0.1)",
            "color": Colors.ERROR,
            "border": f"1px solid rgba(239, 68, 68, 0.2)",
        },
    }
    
    size_config = sizes.get(size, sizes["sm"])
    variant_config = variants.get(variant, variants["default"])
    
    return rx.badge(
        text,
        padding=size_config["padding"],
        font_size=size_config["font_size"],
        font_family=Typography.MONO,
        font_weight=Typography.FONT_MEDIUM,
        border_radius=BorderRadius.RADIUS_FULL,
        **variant_config,
        **props
    )


# ============================================================================
# GLASS DIVIDER
# ============================================================================

def glass_divider(
    **props
) -> rx.Component:
    """
    Glass-styled horizontal divider.
    
    Args:
        **props: Additional props (orientation, margin, etc.)
    
    Returns:
        Glass divider component
    """
    orientation = props.pop("orientation", "horizontal")
    margin = props.pop("margin", f"{"6"} 0")
    
    if orientation == "horizontal":
        return rx.box(
            height="1px",
            width="100%",
            background=f"linear-gradient(90deg, transparent, {Colors.BORDER_MEDIUM}, transparent)",
            margin=margin,
            **props
        )
    else:
        return rx.box(
            width="1px",
            height="100%",
            background=f"linear-gradient(180deg, transparent, {Colors.BORDER_MEDIUM}, transparent)",
            margin=margin,
            **props
        )


# ============================================================================
# GLASS STAT CARD
# ============================================================================

def glass_stat_card(
    title: str,
    value: str | int,
    icon: str,
    **props
) -> rx.Component:
    """
    Glass-styled statistics card.
    
    Args:
        title: Stat card title
        value: Stat card value
        icon: Icon name (from lucide icons)
        **props: Additional props
    
    Returns:
        Glass stat card component
    """
    return glass_card(
        rx.vstack(
            rx.hstack(
                rx.icon(
                    icon,
                    size=24,
                    color=Colors.NEST_ACCENT,
                ),
                rx.text(
                    title,
                    font_size=Typography.TEXT_SM,
                    font_family=Typography.SANS,
                    color=Colors.TEXT_SECONDARY,
                    font_weight=Typography.FONT_MEDIUM,
                ),
                spacing="3",
                align="center",
            ),
            rx.text(
                str(value),
                font_size=Typography.TEXT_5XL,
                font_family=Typography.DISPLAY,
                color=Colors.TEXT_PRIMARY,
                font_weight=Typography.FONT_BOLD,
            ),
            spacing="4",
            align="start",
        ),
        **props
    )


# ============================================================================
# GLASS MODAL
# ============================================================================

def glass_modal(
    *children,
    **props
) -> rx.Component:
    """
    Glass-styled modal component.
    
    Args:
        *children: Child components
        **props: Additional props (is_open, on_close, etc.)
    
    Returns:
        Glass modal component
    """
    is_open = props.pop("is_open", False)
    on_close = props.pop("on_close", None)
    
    return rx.cond(
        is_open,
        rx.box(
            rx.box(
                *children,
                padding="8",
                background=Colors.BG_CARD,
                backdrop_filter="blur(24px)",
                webkit_backdrop_filter="blur(24px)",
                border=f"1px solid {Colors.BORDER_LIGHT}",
                border_radius=BorderRadius.RADIUS_3XL,
                box_shadow=Shadows.SHADOW_2XL,
                max_width="500px",
                width="100%",
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="rgba(0, 0, 0, 0.8)",
            backdrop_filter="blur(4px)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="9999",
            on_click=on_close,
        ),
        rx.box()
    )


# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    "glass_panel",
    "glass_card",
    "glass_button",
    "glass_input",
    "glass_textarea",
    "glass_badge",
    "glass_divider",
    "glass_stat_card",
    "glass_modal",
]