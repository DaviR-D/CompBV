if [ -d "/usr/share/CompBV" ]; then
    rm -r /usr/share/CompBV && rm /usr/share/applications/CompBV.desktop
fi
cp -r CompBV /usr/share && cp CompBV.desktop /usr/share/applications
