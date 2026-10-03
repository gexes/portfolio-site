# Project Dreamscape — enemy tuning note

**Balance pass recorded:** April 11, 2025  
**Author of prefab commit:** Gexes  
**Unity source:** `a5a02976d3d097421be99be79b2158e967509d36` on `Balancing-Brandon`  
**Observation source:** *Enemy Balancing Documentation* (retained in the repository), pages 1–3

This is a retrospective sheet made from the dated Unity prefab diff and the design document. The commit date is verified; the playtest session date is not in the available files. “Before” means the prefab value in the commit's parent, and “after” means the value in the commit. These values document the balancing branch, not a confirmed shipped build.

## Follower — group pressure

**Playtest issue:** Groups of Followers felt too weak and lost pressure too quickly.  
**Reason for the pass:** Keep Followers present in a group fight while lowering damage spikes.

| Prefab field | Before | After |
| --- | ---: | ---: |
| Max health, base value | 50 | 65 |
| Base speed | 2 | 3 |
| Target detection radius | 10 | 14 |
| Base damage range | 10–15 | 7–11 |
| Custom collision offset from ground | 0.5 | 0.8 |

The collision offset also changed in the commit, but the available notes do not state why. The design PDF lists the former damage range as 10–13 and says stagger duration changed to 0.8 seconds; neither matches this prefab diff. Those numbers are not used in the sheet.

## Charger — burst disruption

**Playtest issue:** Burst damage, a long charge, and weak warning made hits difficult to read.  
**Reason for the pass:** Reduce damage and charge duration while giving the player a clearer approach to react to.

| Prefab field | Before | After |
| --- | ---: | ---: |
| Max health, base value | 160 | 200 |
| Target detection radius | 2.25 | 4 |
| Base damage range | 10–15 | 4–12 |
| Entity staggered state duration | 0.5 | 4 |
| Detection distance | 15 | 30 |
| Charge duration | 20 | 8 |
| Jab duration | 0.45 | 0.65 |

The design PDF states that charge contact damage changed, but the prefab diff leaves its multiplier at 2. It also gives different former values for detection distance and stagger duration. The page now describes only the changes supported by the prefab diff.

## Golem — area control

**Playtest issue:** The Golem was easy to interrupt, so its area attack did not force repositioning.  
**Reason for the pass:** Increase staying power and ground smash displacement so the attack can shape movement.

| Prefab field | Before | After |
| --- | ---: | ---: |
| Max health, base value | 200 | 250 |
| Daze damage threshold | 25 | 30 |
| Ground smash launch force | 7.5 | 12 |

The design PDF lists ground smash launch force as 10 after tuning; the dated prefab diff records 12. The note uses 12.

## Source and scope

- Unity prefab files: `Assets/Prefabs/Entities/Enemies/Follower.prefab`, `Charger.prefab`, and `Golem.prefab` in the Project Dreamscape repository.
- Values were checked against `git show a5a02976 -- Assets/Prefabs/Entities/Enemies/{Follower,Charger,Golem}.prefab`.
- The `development` checkout available during this review still contains earlier values. The balancing commit is on `origin/Balancing-Brandon`; this note does not claim that it was merged or shipped.
- The reasons summarize the linked design PDF's identified issues and design rationale. No separate dated QA form or playtest log was found in the available project files.
