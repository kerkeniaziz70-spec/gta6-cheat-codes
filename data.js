/* Name|category|D-pad (U R D L)|How to unlock — add/edit lines here */
const RAW=`$250,000 Money|player|URDLULDR|Finish the story
Drunk|player|ULRUULRULR|Spend $2,500 on alcohol
Unlimited Focus|player|DUUDUDUDUR|Finish the story
No Fall Damage|player|DUUUUUUUD|Survive a freefall from 40 feet 20 times
Parachute|player|RULURULUR|Complete 50 skydives or BASE jumps from 300 ft or higher
Body Armor|player|DULUUUUUDD|Complete 100 workouts
Raise Heat Level|police|LDRDUDU|Lose a 3-star wanted level 25 times
Raise Wanted Level|police|LDRDURU|Lose a 3-star wanted level 50 times
Max Ammo|weapons|DURDLLUUDL|Win 25 bronze medals or better at Shooting Ranges
Infinite Ammo|weapons|DURDLLUDDD|Win 25 silver medals or better at Shooting Ranges
No Reload|weapons|DURDLLUDDU|Win 25 gold medals at Shooting Ranges
All Explosive Weapons|weapons|RULURULUL|Throw 100 grenades
Incendiary Ammo|weapons|DURDLDURDD|Burn 100 enemies with fire damage
Exploding Bottles|weapons|DULLRDDUL|Throw 100 Molotovs
Explosive Shotgun|weapons|DURDLDURDL|Hit 100 enemies with explosive damage
Hauners H-AT|weapons|RULURULUU|Blow up 100 vehicles
Attack Force|weapons|DULLRDDUD|Finish the story
Exploding Balls|weapons|DULLRDDUR|Hit 20 enemies with explosive damage
Vehicle Force|weapons|DULLRDLUD|Kill 25 enemies with a vehicle
Repair Vehicle|vehicles|RDDRDRRD|Win 1st place in 10 races at Gellhorn Raceway, Thrillbilly Mud Club and Boone Speedway
Unlimited Nitrous|vehicles|RDDRDRRL|Complete 50 Stunt Jumps
Spawn Interstate Ambulance|vehicles|LURDLRRR|Discover the Interstate Ambulance (Progress menu)
Spawn Airboat 09|vehicles|LURDLDUR|Complete 5 Survival challenges
Spawn Bravado Banshee|vehicles|LURDLRUL|Complete all Combat challenges
Spawn Tuff BMX|vehicles|LURDLLUR|Complete 5 Fitness challenges
Spawn Maibatsu Boomazoom|vehicles|LURDLLUL|Complete 5 Shopping challenges
Spawn Nagasaki Carbon RS|vehicles|LURDLLUU|Complete all Exploration challenges
Spawn '65 Vapid Dominator|vehicles|LURDLRLR|Complete all Fitness challenges
Spawn Progen Emerus|vehicles|LURDLRUR|Complete all Vehicle challenges
Spawn Inflatable Flamingo|vehicles|LURDLDUD|Destroy 50 cocaine flamingos
Spawn MTL Pumper|vehicles|LURDLRRU|Discover the MTL Pumper (Progress menu)
Spawn Vapid Stanier G2 Taxi|vehicles|LURDLRRL|Complete 5 Sports challenges
Spawn Hauners P-996 Lazer|vehicles|LURDLUUD|Complete all challenges
Spawn HVY Bulldozer|vehicles|LURDLRRD|Discover the HVY Bulldozer (Progress menu)
Spawn Lapwing Mallard|vehicles|LURDLUUU|Complete 5 Vehicle challenges
Spawn Brimstone Golfer|vehicles|LURDLRUD|Complete all Sports challenges
Spawn Hauners Rhino Tank|vehicles|LURDLRLU|Complete all Survival challenges
Spawn Maibatsu Sanchez|vehicles|LURDLLRU|Complete 5 Criminal challenges
Spawn Nagasaki Sea Sparrow|vehicles|LURDLUUR|Complete 5 Exploration challenges
Spawn Speeder 700 GT|vehicles|LURDLDUU|Complete 5 Combat challenges
Spawn Truffade Thrax|vehicles|LURDLRUU|Complete all Shopping challenges
Spawn Western Zombie Bobber|vehicles|LURDLLUD|Complete all Criminal challenges
Move Time Forward|world|DRUDRUU|Find 10 collectible Watches
Pause Time of Day|world|DRUDRUL|Find 20 collectible Watches
Cycle Weather|world|DRUDRUR|Finish the story
Golden Hour Filter|world|DDURRULLUU|Spend 4 hours holding hands
Powdered Sugar Filter|world|DDURRULLUR|Scan all space debris with WAiNK
Pinhole Filter|world|DDURRULLUD|Clear 25 gang operations with your partner
Neon Jungle Filter|world|DDURRULLUL|Discover all 16 Girlypop Vehicles
Yesteryear Filter|world|DDURRULLRU|Discover the Ridgeway
Cataclysm Filter|world|DDURRULLRR|Discover Martha's Vamos (Progress menu)
Videotape Filter|world|DDURRULLRD|Complete 50 activities with your partner
Dark Mirror Filter|world|DDURRULLRL|Make $500,000 selling vehicles
Migraine Filter|world|DDURRULLDU|Survive 6 minutes with a 6-star wanted level
Dollhouse Filter|world|DDURRULLDR|Spend 8 hours with your partner
Bubblegum Filter|world|DDURRULLDD|Find all 24 Vice City Flamingos cards
Fast Forward Filter|world|DDURRULLDL|Complete 50 meditations
Fisheye Filter|world|DDURRULLLU|Catch 100 fish
Faded Glory Filter|world|DDURRULLLR|Rob 50 stores with your partner
Pixel Art Filter|world|DDURRULLLD|Make $250,000 selling collectibles
Hellscape Filter|world|DDURRULLLL|Steal 100 cop vehicles`;
const AR={U:"↑",R:"→",D:"↓",L:"←"};
const C=RAW.split("\n").map(l=>{const[n,c,s,u]=l.split("|");return[n,c,s=="TBA"?"To be announced":[...s].map(x=>AR[x]).join(" "),u||"To be announced"]});
