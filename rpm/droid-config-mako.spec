# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device mako
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 4

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.25

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc

