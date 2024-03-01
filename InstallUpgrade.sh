if [ -d "$HOME/.local/share/CompBV" ]; then
    rm -r $HOME/.local/share/CompBV && rm $HOME/.local/share/applications/CompBV.desktop
fi
cp -r CompBV $HOME/.local/share/ && cp CompBV.desktop $HOME/.local/share/applications

echo Path=$HOME/.local/share/CompBV >> $HOME/.local/share/applications/CompBV.desktop

