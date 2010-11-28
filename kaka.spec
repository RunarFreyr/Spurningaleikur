# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'bootstrap.py'],
             pathex=['/Users/gudbergur/Dropbox/Skoli/Hugbu\xcc\x81na\xc3\xb0arfr\xc3\xa6\xc3\xb0i/verkefni2'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.darwin/kaka', 'kaka'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'kaka'))
