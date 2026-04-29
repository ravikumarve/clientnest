"""
Custom Cursor Component
=======================

Interactive custom cursor with dot and ring effects.
Provides smooth trailing animation and hover state feedback.
"""

import reflex as rx


def custom_cursor() -> rx.Component:
    """
    Custom cursor component with dot and ring.
    
    Returns:
        Custom cursor component
    """
    return rx.fragment(
        # Cursor dot (small, follows immediately)
        rx.box(
            class_name="cursor-dot",
            id="cursor-dot",
            width="8px",
            height="8px",
            background_color="#ffffff",
            border_radius="50%",
            position="fixed",
            pointer_events="none",
            z_index="9999",
            transform="translate(-50%, -50%)",
            box_shadow="0 0 10px rgba(255, 255, 255, 0.8)",
            transition="width 0.2s, height 0.2s",
        ),
        
        # Cursor ring (larger, smooth trailing)
        rx.box(
            class_name="cursor-ring",
            id="cursor-ring",
            width="40px",
            height="40px",
            border="1px solid rgba(255, 255, 255, 0.3)",
            border_radius="50%",
            position="fixed",
            pointer_events="none",
            z_index="9998",
            transform="translate(-50%, -50%)",
            transition="width 0.3s ease, height 0.3s ease, background-color 0.3s ease, border-color 0.3s ease",
        ),
        
        # Custom cursor script
        rx.script("""
            document.addEventListener('DOMContentLoaded', () => {
                const cursorDot = document.getElementById('cursor-dot');
                const cursorRing = document.getElementById('cursor-ring');
                
                let mouseX = window.innerWidth / 2;
                let mouseY = window.innerHeight / 2;
                let ringX = mouseX;
                let ringY = mouseY;
                
                window.addEventListener('mousemove', (e) => {
                    mouseX = e.clientX;
                    mouseY = e.clientY;
                    
                    // Immediate dot update
                    cursorDot.style.left = mouseX + 'px';
                    cursorDot.style.top = mouseY + 'px';
                });
                
                // Handle interactive element hovers for cursor
                const interactives = document.querySelectorAll('a, button, .interactive-hover');
                interactives.forEach(el => {
                    el.addEventListener('mouseenter', () => {
                        cursorDot.style.transform = 'translate(-50%, -50%) scale(0)';
                        cursorRing.style.width = '80px';
                        cursorRing.style.height = '80px';
                        cursorRing.style.backgroundColor = 'rgba(255, 255, 255, 0.05)';
                        cursorRing.style.borderColor = '#ffffff';
                        cursorRing.style.backdropFilter = 'blur(2px)';
                    });
                    el.addEventListener('mouseleave', () => {
                        cursorDot.style.transform = 'translate(-50%, -50%) scale(1)';
                        cursorRing.style.width = '40px';
                        cursorRing.style.height = '40px';
                        cursorRing.style.backgroundColor = 'transparent';
                        cursorRing.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                        cursorRing.style.backdropFilter = 'none';
                    });
                });
                
                // Smooth render loop for ring trailing effect
                const render = () => {
                    // Lerp for cursor ring (smooth trailing effect)
                    ringX += (mouseX - ringX) * 0.15;
                    ringY += (mouseY - ringY) * 0.15;
                    cursorRing.style.left = ringX + 'px';
                    cursorRing.style.top = ringY + 'px';
                    
                    requestAnimationFrame(render);
                };
                
                render();
            });
        """),
    )


def ambient_background() -> rx.Component:
    """
    Ambient background with fluid orbs and parallax effects.
    
    Returns:
        Ambient background component
    """
    return rx.fragment(
        # Ambient fluid container
        rx.box(
            # Primary orb
            rx.box(
                class_name="fluid-orb animate-float-slow",
                id="orb-primary",
                width="60vw",
                height="60vw",
                background="rgba(99, 102, 241, 0.15)",
                top="-20%",
                left="-10%",
            ),
            # Secondary orb
            rx.box(
                class_name="fluid-orb animate-float-delayed",
                id="orb-secondary",
                width="50vw",
                height="50vw",
                background="rgba(139, 92, 246, 0.12)",
                bottom="-10%",
                right="-10%",
            ),
            class_name="ambient-fluid",
        ),
        
        # Noise texture overlay
        rx.box(
            class_name="noise-layer",
        ),
        
        # Parallax script
        rx.script("""
            document.addEventListener('DOMContentLoaded', () => {
                const orbPrimary = document.getElementById('orb-primary');
                const orbSecondary = document.getElementById('orb-secondary');
                
                let orbPrimX = 0, orbPrimY = 0;
                let orbSecX = 0, orbSecY = 0;
                
                window.addEventListener('mousemove', (e) => {
                    const winCenterX = window.innerWidth / 2;
                    const winCenterY = window.innerHeight / 2;
                    const offsetX = (e.clientX - winCenterX) / winCenterX;
                    const offsetY = (e.clientY - winCenterY) / winCenterY;
                    
                    // Subtle inverse movement for parallax effect
                    orbPrimX += ((offsetX * -80) - orbPrimX) * 0.05;
                    orbPrimY += ((offsetY * -80) - orbPrimY) * 0.05;
                    orbSecX += ((offsetX * 60) - orbSecX) * 0.04;
                    orbSecY += ((offsetY * 60) - orbSecY) * 0.04;
                    
                    orbPrimary.style.transform = 'translate(' + orbPrimX + 'px, ' + orbPrimY + 'px)';
                    orbSecondary.style.transform = 'translate(' + orbSecX + 'px, ' + orbSecY + 'px)';
                });
            });
        """),
    )


def interactive_wrapper(*children, **props) -> rx.Component:
    """
    Wrapper component that adds interactive hover class for cursor effects.
    
    Args:
        *children: Child components
        **props: Additional props
    
    Returns:
        Interactive wrapper component
    """
    return rx.box(
        *children,
        class_name="interactive-hover",
        **props
    )


__all__ = [
    "custom_cursor",
    "ambient_background",
    "interactive_wrapper",
]