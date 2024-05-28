use ig_clone;

-- 1 Find the 5 oldest users.
SELECT username, created_at
FROM users
ORDER BY created_at ASC
LIMIT 5;

-- 2 What day of the week do most users register on? We need to figure out when to schedule an ad campaign.
SELECT DAYNAME(created_at) AS day_of_week, COUNT(*) AS registrations
FROM users
GROUP BY day_of_week
ORDER BY registrations DESC
LIMIT 1;

-- 3 We want to target our inactive users with an email campaign.Find the users who have never posted a photo.
SELECT username
FROM users u
LEFT JOIN photos p ON u.id = p.user_id
WHERE p.id IS NULL;

-- 4 Who won the contest for the most likes on a single photo.
SELECT p.id AS photo_id, p.user_id, u.username, COUNT(l.user_id) AS like_count
FROM photos p
JOIN likes l ON p.id = l.photo_id
JOIN users u ON p.user_id = u.id
GROUP BY p.id
ORDER BY like_count DESC
LIMIT 1;

-- 5 How many times does the average user post.
SELECT AVG(photo_count) AS average_posts
FROM (
    SELECT COUNT(*) AS photo_count
    FROM photos
    GROUP BY user_id
) AS photo_counts;

-- 6 User ranking by postings higher to lower.
SELECT u.username, COUNT(p.id) AS post_count
FROM users u
LEFT JOIN photos p ON u.id = p.user_id
GROUP BY u.id
ORDER BY post_count DESC;

-- 7 Total numbers of users who have posted at least one time.
SELECT COUNT(DISTINCT user_id) AS users_with_posts
FROM photos;

-- 8 A brand wants to know which hashtags to use in a post
-- What are the top 5 most commonly used hashtags?

SELECT t.tag_name, COUNT(pt.photo_id) AS usage_count
FROM tags t
JOIN photo_tags pt ON t.id = pt.tag_id
GROUP BY t.tag_name
ORDER BY usage_count DESC
LIMIT 5;

-- 9 We have a small problem with bots on our site...Find users who have liked every single photo on the site.
SELECT u.username
FROM users u
JOIN likes l ON u.id = l.user_id
GROUP BY u.id
HAVING COUNT(l.photo_id) = (SELECT COUNT(*) FROM photos);

-- 10 Find users who have never commented on a photo.
SELECT username
FROM users u
LEFT JOIN comments c ON u.id = c.user_id
WHERE c.id IS NULL;
