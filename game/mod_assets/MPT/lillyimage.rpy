layeredimage lilly:
    group outfit:
        attribute uniform default null
        attribute casual null

    group body:
        attribute norm default if_any(["uniform"]):
            "mod_assets/MPT/lilly/1rl.png"
        attribute think if_any(["uniform"]):
            "mod_assets/MPT/lilly/2rl.png"
        attribute hands if_any(["uniform"]):
            "mod_assets/MPT/lilly/3arl.png"
        attribute cat if_any(["uniform"]):
            "mod_assets/MPT/lilly/3brl.png"
        attribute doll if_any(["uniform"]):
            "mod_assets/MPT/lilly/3drl.png"
        attribute fight if_any(["uniform"]):
            "mod_assets/MPT/lilly/4arl.png"
        attribute middle if_any(["uniform"]):
            "mod_assets/MPT/lilly/4brl.png"
        
        attribute norm default if_any(["casual"]):
            "mod_assets/MPT/lilly/1rlbb.png"
        attribute think if_any(["casual"]):
            "mod_assets/MPT/lilly/2rlbb.png"
        attribute hands if_any(["casual"]):
            "mod_assets/MPT/lilly/3arlbb.png"
        attribute cat if_any(["casual"]):
            "mod_assets/MPT/lilly/3brlbb.png"
        attribute doll if_any(["casual"]):
            "mod_assets/MPT/lilly/3drlbb.png"
        attribute fight if_any(["casual"]):
            "mod_assets/MPT/lilly/4arlbb.png"
        attribute middle if_any(["casual"]):
            "mod_assets/MPT/lilly/4brlbb.png"

    
    
    
    group face:
        
        anchor (0,0) subpixel (True)
        
        attribute a0 default if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll1.png"
        attribute a1 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll1b.png"
        attribute a2 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll1b2.png"
        attribute b0 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll2.png"
        attribute c0 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll3.png"
        attribute c1 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll3b.png"
        attribute c2 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll3b2.png"
        attribute d0 if_any(["doll"]):
            "mod_assets/MPT/lilly/Doll4.png"
        
        
        attribute a1 default:
            "mod_assets/MPT/lilly/a1.png"
        attribute a1c2:
            "mod_assets/MPT/lilly/a1c2.png"
        attribute a1e:
            "mod_assets/MPT/lilly/a1e.png"
        attribute a2:
            "mod_assets/MPT/lilly/a2.png"
        attribute a2c2:
            "mod_assets/MPT/lilly/a2c2.png"
        attribute a2e:
            "mod_assets/MPT/lilly/a2e.png"
        attribute b:
            "mod_assets/MPT/lilly/b.png"
        attribute bc2:
            "mod_assets/MPT/lilly/bc2.png"
        attribute be:
            "mod_assets/MPT/lilly/be.png"
        attribute c1:
            "mod_assets/MPT/lilly/c1.png"
        attribute c1b:
            "mod_assets/MPT/lilly/c1b.png"
        attribute c1bc2:
            "mod_assets/MPT/lilly/c1bc2.png"
        attribute c1c2:
            "mod_assets/MPT/lilly/c1c2.png"
        attribute c1e:
            "mod_assets/MPT/lilly/c1e.png"
        attribute c1eb:
            "mod_assets/MPT/lilly/c1eb.png"
        attribute c2:
            "mod_assets/MPT/lilly/c2.png"
        attribute c2c2:
            "mod_assets/MPT/lilly/c2c2.png"
        attribute c2e:
            "mod_assets/MPT/lilly/c2e.png"
        attribute c3:
            "mod_assets/MPT/lilly/c3.png"
        attribute c3c2:
            "mod_assets/MPT/lilly/c3c2.png"
        attribute c3e:
            "mod_assets/MPT/lilly/c3e.png"
        attribute d:
            "mod_assets/MPT/lilly/d.png"
        attribute db:
            "mod_assets/MPT/lilly/db.png"
        attribute dbc2:
            "mod_assets/MPT/lilly/dbc2.png"
        attribute dc2:
            "mod_assets/MPT/lilly/dc2.png"
        attribute de:
            "mod_assets/MPT/lilly/de.png"
        attribute deb:
            "mod_assets/MPT/lilly/deb.png"
        attribute e:
            "mod_assets/MPT/lilly/e.png"
        attribute eb:
            "mod_assets/MPT/lilly/eb.png"
        attribute ebc2:
            "mod_assets/MPT/lilly/ebc2.png"
        attribute ec2:
            "mod_assets/MPT/lilly/ec2.png"
        attribute ee:
            "mod_assets/MPT/lilly/ee.png"
        attribute eeb:
            "mod_assets/MPT/lilly/eeb.png"
        attribute f1:
            "mod_assets/MPT/lilly/f1.png"
        attribute f1c2:
            "mod_assets/MPT/lilly/f1c2.png"
        attribute f1e:
            "mod_assets/MPT/lilly/f1e.png"
        attribute f2:
            "mod_assets/MPT/lilly/f2.png"
        attribute f2c2:
            "mod_assets/MPT/lilly/f2c2.png"
        attribute f2e:
            "mod_assets/MPT/lilly/f2e.png"
        attribute g:
            "mod_assets/MPT/lilly/g.png"
        attribute gc2:
            "mod_assets/MPT/lilly/gc2.png"
        attribute ge:
            "mod_assets/MPT/lilly/ge.png"
        attribute go1:
            "mod_assets/MPT/lilly/gogogogo1.png"
        attribute go2:
            "mod_assets/MPT/lilly/gogogogo2.png"
        attribute go3:
            "mod_assets/MPT/lilly/gogogogo3.png"
        attribute go4:
            "mod_assets/MPT/lilly/gogogogo4.png"
        attribute go5:
            "mod_assets/MPT/lilly/gogogogo5.png"
        attribute go6:
            "mod_assets/MPT/lilly/gogogogo6.png"
        attribute go7:
            "mod_assets/MPT/lilly/gogogogo7.png"
        attribute h1:
            "mod_assets/MPT/lilly/h1.png"
        attribute h1b:
            "mod_assets/MPT/lilly/h1b.png"
        attribute h1bc2:
            "mod_assets/MPT/lilly/h1bc2.png"
        attribute h1c2:
            "mod_assets/MPT/lilly/h1c2.png"
        attribute h1e:
            "mod_assets/MPT/lilly/h1e.png"
        attribute h1eb:
            "mod_assets/MPT/lilly/h1eb.png"
        attribute h2:
            "mod_assets/MPT/lilly/h2.png"
        attribute h2b:
            "mod_assets/MPT/lilly/h2b.png"
        attribute h2bc2:
            "mod_assets/MPT/lilly/h2bc2.png"
        attribute h2c2:
            "mod_assets/MPT/lilly/h2c2.png"
        attribute h2e:
            "mod_assets/MPT/lilly/h2e.png"
        attribute h2eb:
            "mod_assets/MPT/lilly/h2eb.png"
        attribute i:
            "mod_assets/MPT/lilly/i.png"
        attribute ib:
            "mod_assets/MPT/lilly/ib.png"
        attribute ibc2:
            "mod_assets/MPT/lilly/ibc2.png"
        attribute ic2:
            "mod_assets/MPT/lilly/ic2.png"
        attribute ie:
            "mod_assets/MPT/lilly/ie.png"
        attribute ieb:
            "mod_assets/MPT/lilly/ieb.png"
        attribute j:
            "mod_assets/MPT/lilly/i.png"
        attribute jb:
            "mod_assets/MPT/lilly/ib.png"
        attribute jbc2:
            "mod_assets/MPT/lilly/ibc2.png"
        attribute jc2:
            "mod_assets/MPT/lilly/ic2.png"
        attribute je:
            "mod_assets/MPT/lilly/ie.png"
        attribute jeb:
            "mod_assets/MPT/lilly/ieb.png"
        attribute k:
            "mod_assets/MPT/lilly/k.png"
        attribute kc2:
            "mod_assets/MPT/lilly/kc2.png"
        attribute ke:
            "mod_assets/MPT/lilly/ke.png"
        attribute l1:
            "mod_assets/MPT/lilly/l1.png"
        attribute l1b:
            "mod_assets/MPT/lilly/l1b.png"
        attribute l1b2:
            "mod_assets/MPT/lilly/l1b2.png"
        attribute l1b2c2:
            "mod_assets/MPT/lilly/l1b2c2.png"
        attribute l1bc2:
            "mod_assets/MPT/lilly/l1bc2.png"
        attribute l1c2:
            "mod_assets/MPT/lilly/l1c2.png"
        attribute l1e:
            "mod_assets/MPT/lilly/l1e.png"
        attribute l1eb2:
            "mod_assets/MPT/lilly/l1eb2.png"
        attribute l2:
            "mod_assets/MPT/lilly/l2.png"
        attribute l2b:
            "mod_assets/MPT/lilly/l2b.png"
        attribute l2b2:
            "mod_assets/MPT/lilly/l2b2.png"
        attribute l2b2c2:
            "mod_assets/MPT/lilly/l2b2c2.png"
        attribute l2bc2:
            "mod_assets/MPT/lilly/l2bc2.png"
        attribute l2c2:
            "mod_assets/MPT/lilly/l2c2.png"
        attribute l2e:
            "mod_assets/MPT/lilly/l2e.png"
        attribute l2eb:
            "mod_assets/MPT/lilly/l2eb.png"
        attribute l2eb2:
            "mod_assets/MPT/lilly/l2eb2.png"
        attribute m:
            "mod_assets/MPT/lilly/m.png"
        attribute mb:
            "mod_assets/MPT/lilly/mb.png"
        attribute mb2:
            "mod_assets/MPT/lilly/mb2.png"
        attribute mb2c2:
            "mod_assets/MPT/lilly/mb2c2.png"
        attribute mbc2:
            "mod_assets/MPT/lilly/mbc2.png"
        attribute mc2:
            "mod_assets/MPT/lilly/mc2.png"
        attribute me:
            "mod_assets/MPT/lilly/me.png"
        attribute meb:
            "mod_assets/MPT/lilly/meb.png"
        attribute meb2:
            "mod_assets/MPT/lilly/meb2.png"
        attribute n1:
            "mod_assets/MPT/lilly/n1.png"
        attribute n1b:
            "mod_assets/MPT/lilly/n1b.png"
        attribute n1b2:
            "mod_assets/MPT/lilly/n1b2.png"
        attribute n1b2c2:
            "mod_assets/MPT/lilly/n1b2c2.png"
        attribute n1bc2:
            "mod_assets/MPT/lilly/n1bc2.png"
        attribute n1c2:
            "mod_assets/MPT/lilly/n1c2.png"
        attribute n1e:
            "mod_assets/MPT/lilly/n1e.png"
        attribute n1eb2:
            "mod_assets/MPT/lilly/n1eb2.png"
        attribute n2:
            "mod_assets/MPT/lilly/n2.png"
        attribute n2b:
            "mod_assets/MPT/lilly/n2b.png"
        attribute n2b2:
            "mod_assets/MPT/lilly/n2b2.png"
        attribute n2b2c2:
            "mod_assets/MPT/lilly/n2b2c2.png"
        attribute n2bc2:
            "mod_assets/MPT/lilly/n2bc2.png"
        attribute n2c2:
            "mod_assets/MPT/lilly/n2c2.png"
        attribute n2e:
            "mod_assets/MPT/lilly/n2e.png"
        attribute n2eb2:
            "mod_assets/MPT/lilly/n2eb2.png"
        attribute n4:
            "mod_assets/MPT/lilly/n4.png"
        attribute n4b:
            "mod_assets/MPT/lilly/n4b.png"
        attribute n4b2:
            "mod_assets/MPT/lilly/n4b2.png"
        attribute n4b2c2:
            "mod_assets/MPT/lilly/n4b2c2.png"
        attribute n4bc2:
            "mod_assets/MPT/lilly/n4bc2.png"
        attribute n4c2:
            "mod_assets/MPT/lilly/n4c2.png"
        attribute n4e:
            "mod_assets/MPT/lilly/n4e.png"
        attribute n4eb:
            "mod_assets/MPT/lilly/n4eb.png"
        attribute n4eb2:
            "mod_assets/MPT/lilly/n4eb2.png"
        attribute o:
            "mod_assets/MPT/lilly/o.png"
        attribute ob:
            "mod_assets/MPT/lilly/ob.png"
        attribute ob2:
            "mod_assets/MPT/lilly/ob2.png"
        attribute ob2c2:
            "mod_assets/MPT/lilly/ob2c2.png"
        attribute obc2:
            "mod_assets/MPT/lilly/obc2.png"
        attribute oc2:
            "mod_assets/MPT/lilly/oc2.png"
        attribute oe:
            "mod_assets/MPT/lilly/oe.png"
        attribute oeb:
            "mod_assets/MPT/lilly/oeb.png"
        attribute p:
            "mod_assets/MPT/lilly/p.png"
        attribute pb:
            "mod_assets/MPT/lilly/pb.png"
        attribute pb2:
            "mod_assets/MPT/lilly/pb2.png"
        attribute pb2c2:
            "mod_assets/MPT/lilly/pb2c2.png"
        attribute pbc2:
            "mod_assets/MPT/lilly/pbc2.png"
        attribute pc2:
            "mod_assets/MPT/lilly/pc2.png"
        attribute pe:
            "mod_assets/MPT/lilly/pe.png"
        attribute peb:
            "mod_assets/MPT/lilly/peb.png"
        attribute q:
            "mod_assets/MPT/lilly/q.png"
        attribute qb:
            "mod_assets/MPT/lilly/qb.png"
        attribute qb2:
            "mod_assets/MPT/lilly/qb2.png"
        attribute qb2c2:
            "mod_assets/MPT/lilly/qb2c2.png"
        attribute qbc2:
            "mod_assets/MPT/lilly/qbc2.png"
        attribute qc2:
            "mod_assets/MPT/lilly/qc2.png"
        attribute qe:
            "mod_assets/MPT/lilly/qe.png"
        attribute qeb:
            "mod_assets/MPT/lilly/qeb.png"
        attribute r1:
            "mod_assets/MPT/lilly/r1.png"
        attribute r1c2:
            "mod_assets/MPT/lilly/r1c2.png"
        attribute r1e:
            "mod_assets/MPT/lilly/r1e.png"
        attribute r2:
            "mod_assets/MPT/lilly/r2.png"
        attribute r2c2:
            "mod_assets/MPT/lilly/r2c2.png"
        attribute r2e:
            "mod_assets/MPT/lilly/r2e.png"
        attribute s:
            "mod_assets/MPT/lilly/s.png"
        attribute sadc1:
            "mod_assets/MPT/lilly/Sadistic1.png"
        attribute sadc1e1:
            "mod_assets/MPT/lilly/Sadistic1e1.png"
        attribute sadc1e2:
            "mod_assets/MPT/lilly/Sadistic1e2.png"
        attribute sadc2:
            "mod_assets/MPT/lilly/Sadistic2.png"
        attribute sadc2e1:
            "mod_assets/MPT/lilly/Sadistic2e1.png"
        attribute sadc2e2:
            "mod_assets/MPT/lilly/Sadistic2e2.png"
        attribute sadc3:
            "mod_assets/MPT/lilly/Sadistic3.png"
        attribute sadc3e1:
            "mod_assets/MPT/lilly/Sadistic3e1.png"
        attribute sadc3e2:
            "mod_assets/MPT/lilly/Sadistic3e2.png"
        attribute sadc4:
            "mod_assets/MPT/lilly/Sadistic4.png"
        attribute sadc4e1:
            "mod_assets/MPT/lilly/Sadistic4e1.png"
        attribute sadc4e2:
            "mod_assets/MPT/lilly/Sadistic4e2.png"
        attribute sadc5:
            "mod_assets/MPT/lilly/Sadistic5.png"
        attribute sadc5e1:
            "mod_assets/MPT/lilly/Sadistic5e1.png"
        attribute sadc5e2:
            "mod_assets/MPT/lilly/Sadistic5e2.png"
        attribute sadc6e1:
            "mod_assets/MPT/lilly/Sadistic6e1.png"
        attribute sadc6e2:
            "mod_assets/MPT/lilly/Sadistic6e2.png"
        attribute sadck:
            "mod_assets/MPT/lilly/SadisticKero.png"
        attribute sadcke1:
            "mod_assets/MPT/lilly/SadisticKeroe1.png"
        attribute sadcke2:
            "mod_assets/MPT/lilly/SadisticKeroe2.png"
        attribute sc:
            "mod_assets/MPT/lilly/sc.png"
        attribute se:
            "mod_assets/MPT/lilly/se.png"
        attribute ssh:
            "mod_assets/MPT/lilly/Ssh!.png"
        attribute t2:
            "mod_assets/MPT/lilly/t2.png"
        attribute t2c2:
            "mod_assets/MPT/lilly/t2c2.png"
        attribute t2e:
            "mod_assets/MPT/lilly/t2e.png"
        attribute t3:
            "mod_assets/MPT/lilly/t3.png"
        attribute t3c2:
            "mod_assets/MPT/lilly/t3c2.png"
        attribute t3e:
            "mod_assets/MPT/lilly/t3e.png"
        attribute tong1:
            "mod_assets/MPT/lilly/tong1.png"
        attribute tong1c2:
            "mod_assets/MPT/lilly/tong1c2.png"
        attribute tong2:
            "mod_assets/MPT/lilly/tong2.png"
        attribute tong2b:
            "mod_assets/MPT/lilly/tong2b.png"
        attribute tong2bc2:
            "mod_assets/MPT/lilly/tong2bc2.png"
        attribute tong2c2:
            "mod_assets/MPT/lilly/tong2c2.png"
        attribute tong3:
            "mod_assets/MPT/lilly/tong3.png"
        attribute tong3b:
            "mod_assets/MPT/lilly/tong3b2.png"
        attribute tong3bc2:
            "mod_assets/MPT/lilly/tong3b2c2.png"
        attribute tong3c2:
            "mod_assets/MPT/lilly/tong3c2.png"
        attribute tong4:
            "mod_assets/MPT/lilly/tong4.png"
        attribute tong4b:
            "mod_assets/MPT/lilly/tong4b.png"
        attribute tonge1:
            "mod_assets/MPT/lilly/tonge1.png"
        attribute tonge2:
            "mod_assets/MPT/lilly/tonge2.png"
        attribute tonge2b:
            "mod_assets/MPT/lilly/tonge2b.png"
        attribute tonge3:
            "mod_assets/MPT/lilly/tonge3.png"
        attribute tonge3b2:
            "mod_assets/MPT/lilly/tong3b2.png"
        attribute tonge4:
            "mod_assets/MPT/lilly/tonge4.png"
        attribute tonge4b:
            "mod_assets/MPT/lilly/tonge4b.png"
        attribute u:
            "mod_assets/MPT/lilly/u.png"
        attribute ub:
            "mod_assets/MPT/lilly/ub.png"
        attribute ub2:
            "mod_assets/MPT/lilly/ub2.png"
        attribute ub2c2:
            "mod_assets/MPT/lilly/ub2c2.png"
        attribute ubc2:
            "mod_assets/MPT/lilly/ubc2.png"
        attribute uc2:
            "mod_assets/MPT/lilly/uc2.png"
        attribute ue:
            "mod_assets/MPT/lilly/ue.png"
        attribute ueb:
            "mod_assets/MPT/lilly/ueb.png"
        attribute ueb2:
            "mod_assets/MPT/lilly/ueb2.png"
        attribute v:
            "mod_assets/MPT/lilly/v.png"
        attribute vb:
            "mod_assets/MPT/lilly/vb.png"
        attribute vb2:
            "mod_assets/MPT/lilly/vb2.png"
        attribute vb2c2:
            "mod_assets/MPT/lilly/vb2c2.png"
        attribute vbc2:
            "mod_assets/MPT/lilly/vbc2.png"
        attribute vc2:
            "mod_assets/MPT/lilly/vc2.png"
        attribute ve:
            "mod_assets/MPT/lilly/ve.png"
        attribute veb:
            "mod_assets/MPT/lilly/veb.png"
        attribute veb2:
            "mod_assets/MPT/lilly/veb2.png"
        attribute w1:
            "mod_assets/MPT/lilly/w1.png"
        attribute w1b:
            "mod_assets/MPT/lilly/w1b.png"
        attribute w1b2:
            "mod_assets/MPT/lilly/w1b2.png"
        attribute w1b2c2:
            "mod_assets/MPT/lilly/w1b2c2.png"
        attribute w1bc2:
            "mod_assets/MPT/lilly/w1bc2.png"
        attribute w1c2:
            "mod_assets/MPT/lilly/w1c2.png"
        attribute w1e:
            "mod_assets/MPT/lilly/w1e.png"
        attribute w1eb:
            "mod_assets/MPT/lilly/w1eb.png"
        attribute w1eb2:
            "mod_assets/MPT/lilly/w1eb2.png"
        attribute w3:
            "mod_assets/MPT/lilly/w3.png"
        attribute w3b:
            "mod_assets/MPT/lilly/w3b.png"
        attribute w3b2:
            "mod_assets/MPT/lilly/w3b2.png"
        attribute w3b2c2:
            "mod_assets/MPT/lilly/w3b2c2.png"
        attribute w3bc2:
            "mod_assets/MPT/lilly/w3bc2.png"
        attribute w3c2:
            "mod_assets/MPT/lilly/w3c2.png"
        attribute w3e:
            "mod_assets/MPT/lilly/w3e.png"
        attribute w3eb:
            "mod_assets/MPT/lilly/w3eb.png"
        attribute w3eb2:
            "mod_assets/MPT/lilly/w3eb2.png"
        attribute x:
            "mod_assets/MPT/lilly/x.png"
        attribute xe:
            "mod_assets/MPT/lilly/xe.png"
        attribute xe2:
            "mod_assets/MPT/lilly/xe2.png"
        attribute y:
            "mod_assets/MPT/lilly/y.png"
        attribute ye:
            "mod_assets/MPT/lilly/ye.png"
        attribute ye2:
            "mod_assets/MPT/lilly/ye2.png"
        attribute z:
            "mod_assets/MPT/lilly/z.png"
        attribute ze:
            "mod_assets/MPT/lilly/ze.png"
        attribute ze2:
            "mod_assets/MPT/lilly/ze2.png"