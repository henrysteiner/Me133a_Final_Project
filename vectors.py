posX = joint.X
poxY = joint.Y
posZ = joint.Z

if joint.ID == 1:
   xs = list((posX, posX + 1))
   ys = list((posY, posY))
   zs = list((posZ, posZ))
   self.ax.plot(xs, ys, zs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   ys = list((posY, posY + 1))
   xs = list((posX, posX))
   zs = list((posZ, posZ))
   self.ax.plot(xs, ys, zs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   zs = list((posZ, posZ + 1))
   xs =list((posX, posX))
   ys = list((posY, posY))
   self.ax.plot(xs, ys, zs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
elseif joint.type == 1:
   xs = list((posX, posX + 1))
   ys = list((posY, posY))
   zs = list((posZ, posZ))
   self.ax.plot(xs, ys, zs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   ys = list((posY, posY - 1))
   xs = list((posX, posX))
   zs = list((posZ, posZ))
   self.ax.plot(xs, zs, ys, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   zs = list((posZ, posZ + 1))
   xs =list((posX, posX))
   ys = list((posY, posY))
   self.ax.plot(xs, zs, ys, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
elseif joint.type == 0:
   xs = list((posX, posX + 1))
   ys = list((posY, posY))
   zs = list((posZ, posZ))
   self.ax.plot(ys, xs, zs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   ys = list((posY, posY + 1))
   xs = list((posX, posX))
   zs = list((posZ, posZ))
   self.ax.plot(xs, zs, ys, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
   zs = list((posZ, posZ + 1))
   xs =list((posX, posX))
   ys = list((posY, posY))
   self.ax.plot(zs, ys, xs, 'o-', markersize=4, 
                     markerfacecolor="blue", linewidth = 1, color="silver")
