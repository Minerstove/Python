subtasks = {
    "Subtask 1": {
        "points": 100,
        "cases": [
            (('.',), "1CCW",),
            (('1223','345E','ABCD','GFTH'), "1F",),
            (('1223','345E','ABCD','GFTH'), "2F",),
            (('1223','345E','ABCD','GFTH'), "1CW",),
            (('1223','345E','ABCD','GFTH'), "1CCW",),
            (('1223','345E','ABCD','GFTH'), "1FL",),
            (('1223','345E','ABCD','GFTH'), "1FR",),
            (('1223','345E','ABCD','GFTH'), "99FL",),
            (('1223','345E','ABCD','GFTH'), "1FL.1FL.1FL",),
            (('1223','345E','ABCD','GFTH'), "5CCW.4CW.5FR.1F.4FL",),
            (('1223','345E','ABCD','GFTH'), "5CCW.4CW.5FR.1F.4FL",),
            (('1223','345E','ABCD','GFTH'), "10CCW.19CW.18FR.17F.16FL",),
            (('1223','345E','ABCD','GFTH'), "5CCW.4CW.5FR.1F.4FL",),
        ]
    },
    "Subtask 2": {
        "points": 100,
        "cases": [
            (('1223','345E','ABCD','GFTH'), "5CCW.4CW.5FR.3TT.1F.4FL",),
            (('1223','345E','ABCD','GFTH'), "10CCW.19CW.18FR.3TT.17F.16FL",),
            (('1223','345E','ABCD','GFTH'), "5CCW.9TT.4CW.5FR.3TT.1F.4FL.1TT",),
            (('1223','345E','ABCD','GFTH'), "100TT",),
            (('1223','345E','ABCD','GFTH'), "49CCW.49TT",),
        ]
    },
    "Subtask 3": {
        "points": 200,
        "cases": [
            ((("ABCDE12345"*5+"abcref1234"*5),)*50+(("123456789a"*5+"GHEJK09876"*5),)*50, "51234431CCW.5TT.41233441CW.394934TT.51231341FR.23334211F.44431132FL.1TT",),
            ((("ABCDE12345"*5+"abcref1234"*5),)*50+(("123456789a"*5+"GHEJK09876"*5),)*50,"51234432CCW.5TT.41233233CW.394934TT.51231341FR.23332211F.4441132FL.1TT",),
            ((("ABCDE12345"*5+"abcref1234"*5),)*50+(("123456789a"*5+"GHEJK09876"*5),)*50,"1CW."*249+"1CW",),
        ]
    }
}
