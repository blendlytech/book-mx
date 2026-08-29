# Chapter 30 — The Beautiful Rendering
So I started selling websites.

It's what I had. A man with a phone, a laptop, and a gift for talking a stranger into something — that man can always find a thing to sell, and websites were the thing that spring. I'd cold-walk the small businesses of Puerto Peñasco. It was a tourist town, so the majority of them had bilingual staff. I'd walk into the taco stands and the dive shops and the little tiendas that sold sunblock and cervezas to the Arizona tourists, and I'd tell them what I told everybody about everything: that they were leaving money on the table, that I could fix it, that it wouldn't cost them much. A couple hundred bucks a build. Maybe one a week if the week was kind. It wasn't good money. It wasn't even good-enough money. It was *scrape by by the skin of your teeth* money, the kind you spend before it clears, but we were doing it — rent covered, food on the table, a beer or two poured into the Yetis at night where the girl couldn't see — and after the call center died and the residual went into the ground with Zaul, *doing it* felt like a kind of winning.

I want to be honest that I was still telling myself the old story through all of it. The dial in my hand. The basement scrubbed clean. Two beers and stop, every night, like proof. A man drowning will call the water he's still treading *swimming*, and I called it swimming.

---

Then in April her mother came up to see us.

It's a three-hour run from Mexicali to Peñasco, straight across the top of the Gulf, and Rose made it the way Rose made everything — alone, no fuss, a woman who'd done eight years in an Arizona federal prison and gotten deported the day she walked out and didn't have a soft edge left anywhere on her. She stayed half a day. Sat with her daughter and her granddaughter, ate something, looked America over the way grandmothers do to make sure the kid was being kept right. And then, because she didn't like to drive that road in the dark, she pointed the car back north before the afternoon was gone.

She was coming around a curve somewhere out in that empty country when the sun caught her. You know that stretch of late light where the whole windshield goes to white and the road just *vanishes* — and she was already in the turn, already committed, and by the time the world came back there wasn't any road under her. The car went off and found a tree.

It punctured her lung. Broke both her legs and an arm. When the call came through it came in the shape all the worst calls come in — not the details, just the weight of it, Glenda's face going to a color I'd never seen on her — and for a stretch of hours nobody could tell us whether the woman was going to live. The woman who'd looked me dead in the eye and asked me to keep her daughter sober. Broken to pieces on the side of a road she'd driven multiple times, because the sun came around a curve at the wrong second.

---

We moved to Mexicali.

There wasn't a conversation about it, not really. You don't sit your family down and weigh the options when Rose is in a hospital bed with a tube in her chest. You pack the car. We folded up the little Peñasco life — the beach, America's school, the scrape-by website hustle, the closest thing to peace I'd had since I was a boy — and we hauled it three hours inland to Rose's house, and we moved in to take care of her.

We were there about four months.

And here is the thing I've turned over a hundred times since. Every other move in this whole book had been *mine* — my warrant, my next angle, my geographic cure, me running from the leaving before the leaving could be done to me. This one wasn't. For the first time in my adult life I picked a family up and carried it somewhere not to save my own skin but to go wipe a broken woman's chin and help her to the toilet and sit with her through the long bright Mexicali afternoons while she healed. Glenda did the real work of it, the daughter's work, the changing and the nursing. I did the rest. And the whole time I was sleeping under the roof of the one person on earth who'd ever asked me for a single thing — *keep her sober* — and drinking my two-beers-and-stop out of a steel cup in her kitchen so her granddaughter wouldn't see. A man can be doing a good and decent thing with his hands and failing somebody quietly the whole time he does it. I was. I'd tell you I didn't see it that way then, but I think I did. I think I always did. I just had the dial-lie loud enough to drink over.

---

It was in that house, those four months, that I finally built the thing.

I have to back up to tell it right, because the building of it goes back years. I'd been messing with AI since the garage in Michigan, since 2022, since back when Glenda used to roll her eyes at a new world-changing idea every single month and watch me drop it by the next. I genuinely had been coding apps with the models before *coding apps with the models* was a thing anyone had a cute name for — and it was ugly work. I'd sit there in the OpenAI Playground describing what I wanted in plain English, getting back a slab of code, pasting it into my editor where Copilot and Tabnine would autocomplete the wiring, and if the thing ran, I kept it. I'd learned some real code along the way. Not enough. Never enough to stand up a whole functioning B2B application by myself, not even close.

Then vibe coding came around, the way it came around for everybody all at once that year, and the tools got good enough to close the gap my own skull couldn't. And I built a real one. Start to finish. Actually finished the damn thing, which if you knew me you'd understand is the rarest sentence in this book.

It was called Brewmetrics, and the idea was genuinely good. I'll die on that hill.

A web platform for craft breweries. It gave them a backend to manage their recipes and their batches, and every batch spat out its own unique QR code that the brewery could print directly onto a coaster. A patron picks up their pint, scans the coaster, and gets pulled into the whole thing — the story behind that beer, the grain bill, the hop profile, why the brewmaster made the calls he made. Then it walked them through a guided tasting. Taught a regular drinker how to evaluate a beer like a professional. Asked them structured questions about the flavor, the mouthfeel, the aroma, and explained why each question mattered to the man who'd brewed it. And then it took all those answers, from every patron, and compiled and scored and published them — so for the first time a brewery had real, public, per-batch consumer data on every single thing they poured.

The breweries lost their minds over it. I signed up forty-three of them at forty-nine bucks a month in the first month, and I hadn't even launched yet. I made the marketing videos with AI, and I'll tell you they were *good* — slick, hungry, the kind of thing that makes a brewmaster feel seen. Forty-three accounts. Recurring. Pre-launch.

I thought I'd made it. God help me, I thought it again. Same exact thought I'd had on that beach about Zaul's machine right before the man walked off the edge of the earth and took it with him. *I've built a thing that lasts.* You'd think a man learns. You'd think.

---

Here's the part I don't love saying out loud.

My whole workflow was what they'd now politely call vibe coding, just uglier and lonelier — describe what I wanted to the model, take the block of code it handed back, paste it in, let the autocomplete finish the sentence, and if it ran clean I shipped it. I did not deeply understand half of what was being generated. I want to be plain about that. It worked. The tests passed. The features did the thing they were supposed to do when I clicked the buttons. And that was good enough for me, because it had always been good enough for me — *looks right, runs clean, ship it* is not just how I built that app. It is how I built every single thing I have ever built, including the man typing this.

Then came day three after launch.

One of my breweries — a popular taproom up in Arizona — decided to throw a launch party for the app. Printed the QR coasters, hyped the whole thing on their socials, packed the house wall to wall. I found out it was happening when my phone started buzzing on the kitchen counter in Rose's house.

Not with congratulations. With error alerts.

Too many people scanning too many codes at the same second. The app buckled almost the instant the crowd hit it. Submissions started timing out. The database started choking. And then it just — went down. All the way down. Not for that one brewery. For all forty-three of them at once.

I spent the next six hours in a full-body panic trying to drag it back online, and that's where the real horror started, because the real horror wasn't the outage. It was what I saw when I finally went into the code to find the wound. Code the model had generated. Code the autocomplete had finished. Code I had accepted and shipped because it looked right and ran clean — and reading back through it at three in the morning in my girlfriend's mother's house, I understood the rot went so much deeper than a traffic spike.

The authorization logic was held together with duct tape. The user sessions were barely implemented. The cloud storage I'd essentially hardcoded for the little volume I'd tested with, never once thinking about what happens when two hundred drunk people at a taproom all start submitting tasting notes at the same time while arguing about whether a hazy IPA has *notes of citrus*. And the security — I don't even want to put this in a book — the thing was so wide open that anybody with a browser console and ten minutes of curiosity could've walked straight into the brewery data, the customer submissions, all of it. Front door off the hinges. Nothing underneath.

I didn't have a crashed app. I had a liability.

I spent the next week writing the most humbling emails of my life to forty-three brewery owners who had handed me their money and their customers' information on the strength of a slick video and a smooth-talking gringo, and trusted that there was something solid behind it. There wasn't. There was a beautiful front end and a hollow behind it, and the first real weight that leaned on it went straight through.

---

I've thought a lot, since, about why that one stuck the knife in deeper than losing the call center did. Zaul vanishing was a thing that happened *to* me — a man disappeared, the machine died, the wheels came off the way wheels do. But Brewmetrics I built with my own hands. And when I finally sat in the wreck of it and looked at what I'd actually made — the gorgeous skin over the nothing, the thing that worked perfectly right up until something real asked something real of it — I wasn't looking at an app anymore.

The model writes code the way a first-year architecture student designs a building. The rendering is beautiful. The light comes through the windows just so. You just can't live in it yet, because nobody's drawn the part that holds the roof up, and you don't find that out until the day it's full of people.

That was the app. It was also, every word of it, me. A beautiful rendering with no idea what was holding it up. *Looks right, runs clean, ship it.* My sobriety was vibe-coded. My whole *I've got it beat* was a front end over a basement I'd never once gone down into. And every few months something real would lean on it — a man vanishing, a mother through a windshield, a launch party, a curve full of sun — and it would go straight to the floor, all forty-three of me at once, and I would sit in the wreckage at three in the morning genuinely shocked, every time, that the thing I'd never built right hadn't held.

We were still in Mexicali when the dust of it settled. Rose was mending. The websites were dead, the app was dead, the residual was long dead. And I did the only thing I knew how to do with a fresh pile of ruin — I started looking for the next thing to ship, grinning, certain, the dial right there in my hand where it had always been, dead wrong about absolutely everything, and pointed, though I couldn't have told you it yet, straight back to the states.
