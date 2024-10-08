## Average Pitch Speed by Pitch Type at Stadium Venues

This section includes an SQL solution for querying baseball pitch data. Specifically, the query retrieves the average pitch speed by pitch type for games that took place in venues containing the word 'Stadium' in their name.

### Data Structure:
- Person: Contains details of the players such as name and batting/pitching hand.
- Venue: Contains details of the venues where events occurred.
- Event: Represents specific games held at the venues.
- Play: Contains pitch details such as speed and type for each player.

### SQL Query:
The query joins these tables to generate a list of player names with their average pitch speed grouped by pitch type, but only for events held at stadiums.

```
SELECT  
    p.fullname,  
    pl.PitchTypeCode,  
    ROUND(AVG(pl.PitchSpeed), 2) AS AvgPitchSpeed 
FROM  
    play pl 
JOIN  
    events e ON pl.EventId = e.EventId 
JOIN  
    (SELECT * FROM venue WHERE name ILIKE '%stadium%') v ON e.VenueId = v.VenueId 
JOIN  
    person p ON pl.PersonId = p.PersonId 
GROUP BY  
    p.fullname,  
    pl.PitchTypeCode 
ORDER BY p.fullname;
```

### Key Features:
- Filters venues to include only those with "Stadium" in their name using a case-insensitive search.
- Groups data by pitcher name and pitch type to calculate the average pitch speed.
- Results are ordered alphabetically by pitcher name.
