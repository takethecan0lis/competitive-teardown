# Desk research source checklist

Work through every source group the depth calls for. Record what was found and what was not found.

## 1. Company's own words (DOCUMENTED)
- Help center or knowledge base: extract the full corpus (help-center-extractor skill).
- App store listings (iOS, Android, Mac, Windows): description, what's new history, version and build, size, rating counts, privacy label, in-app purchase list, age rating.
- Pricing page and paywall copy; free versus paid matrix.
- Privacy policy, terms, data deletion path; compare the store privacy label to the policy and to observed permissions.
- Public company docs (Notion, GitBook, blog, changelog, status page, FAQs about past changes). Change-rationale FAQs are gold: they reveal strategy, metrics, and scars.
- Job posts (current and archived): tech stack, team size, roadmap hints, platform debt.
- Press kit, founder interviews, podcasts, conference talks.
- Trademark registrations (USPTO and others): classes, dates, owner address.

## 2. Third parties (REPORTED)
- Review analytics: themes with counts and date range; sample paraphrased complaints and delights. Prefer aggregate tools over cherry-picked quotes.
- Community: Reddit, Discord, Facebook groups, forums. Note reactions to past changes.
- App intelligence estimates (downloads, revenue, geography): always Low confidence.
- Security and privacy scanners (tracker reports, permissions audits).
- Press and analyst coverage; awards and store features.

## 3. Name collisions
Search for other companies with the same name and exclude them explicitly. Note the exclusion in company-and-history.md.

## Access fallback ladder (try in order; never bypass a site's restrictions)
1. Official API or export (help center API, data export, RSS).
2. WebFetch of the page.
3. A real browser session (built-in browser or Chrome) for JavaScript-rendered pages; reading the page's own public data calls is fine.
4. Driving the product's screen (computer use or iPhone Mirroring).
5. Guided handoff: ask the user to open, export, record, or paste.
If a site refuses access, say so and use another source. Do not use mirrors or caches to get around a refusal.
