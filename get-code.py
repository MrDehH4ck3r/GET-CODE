#!/usr/bin/env python
import base64
#decode the script
exec(base64.b64decode("IyEvdXNyL2Jpbi9weXRob24KIyAqLSogY29kaW5nOiBVVEYtOCAqLSoKIyBUb29sIGJ5IE1yIERlaCBINGNrM3IKIyBweXRob24gdmVyc2lvbiAzLjExLjIKI2NvcHlyaWdodCAoYykgTXIgRGVoIEg0Y2szcgplcnJNc2cgPSBsYW1iZGEgc21zOiAiRXJyb3IiCnRyeToKICAgIGltcG9ydCByZXF1ZXN0cwpleGNlcHQgSW1wb3J0RXJyb3I6CiAgICBlcnJNc2coIlsgcmVxdWVzdHMgXSBtb2R1bGUgaXMgbWlzc2luZyIpCiAgICBwcmludCgiICBbKl0gUGxlYXNlIFVzZTogJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyB0byBpbnN0YWxsIGl0IDopIikKaW1wb3J0IG9zLCB0aW1lCmZyb20gb3MgaW1wb3J0IHN5c3RlbQpmcm9tIG9wdHBhcnNlIGltcG9ydCBPcHRpb25QYXJzZXIKc21zID0gIlwwMzNbMDszMW1kcm9wIHRoZSB0YXJnZXQgd2Vic2l0ZVwwMzNbMDszN20iCnNtczEgPSAiXDAzM1swOzMxbWRyb3AgdGhlIGZpbGUgbmFtZVwwMzNbMDszN20iCm9zLnN5c3RlbSgnY2xlYXInKQp0aW1lLnNsZWVwKDEpCiNoZWxwIG1lc3NhZ2UgYW5kIGJhbm5lciBvZiB0aGUgdG9vbApvcHRpb24gPSBPcHRpb25QYXJzZXIoIiIiCgpcMDMzWzE7MzFt4pae4paA4paW4pab4paA4paY4paA4pab4paYIFwwMzNbMTszMW0g4pae4paA4paW4pae4paA4paW4pab4paA4paW4pab4paA4paYClwwMzNbMTszNm3iloziloTilpbilpniloQgIOKWjOKWhOKWhOKWluKWjCAg4paMIOKWjOKWjCDilozilpniloRcMDMzWzE7MzZtClwwMzNbMTszNG3ilowg4paM4paMICAg4paMICAg4paMIOKWluKWjCDilozilowg4paM4paMCuKWneKWgCDiloDiloDilpgg4paYICAg4pad4paAIOKWneKWgCDiloDiloAg4paA4paA4paYXDAzM1swOzM3bQpQeXRob24gdmlld2VyIGNvZGUgc291cmNlIFtIVE1MXQpcMDMzWzE7OTJtVG9vbCBieTpcMDMzWzA7OTdtIE1yIERlaCBINGNrM3IKXDAzM1sxOzkybWZhY2Vib29rOlwwMzNbMDs5N20gZmFjZWJvb2suY29tL2RhbmkuZWRlbi41NApcMDMzWzE7OTJtRmFjZWJvb2stcGFnZTpcMDMzWzA7OTdtIGZhY2Vib29rLmNvbS9FZGVueUhhY2tlcgpcMDMzWzE7OTJtZW1haWw6XDAzM1swOzk3bSBlZGVuZGFuaWVsNjRAZ21haWwuY29tClwwMzNbMTs5Mm1UZWxlZ3JhbTpcMDMzWzA7OTdtIGh0dHBzOi8vdC5tZS9kZWhoNGNrM3IKXDAzM1sxOzMybUdpdGh1YjpcMDMzWzA7MzdtIGh0dHBzOi8vZ2l0aHViLmNvbS9EZWhINGNrM3JcMDMzWzA7MzdtCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tClsrXSBIRUxQCnB5dGhvbiBnZXQtY29kZS5weSAtaAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpbK10gVVNBR0UKcHl0aG9uIGdldC1jb2RlLnB5IC1sIDx0YXJnZXQgbGluaz4gLWYgPHlvdXIgZmlsZSBuYW1lPgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojIyNFeGVtcGxlOgoKcHl0aG9uIGdldC1jb2RlLnB5IC1sIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiAtZiBGYWNlYm9vawotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpweXRob24gZ2V0LWNvZGUucHkgLS1saW5rIGh0dHBzOi8vd3d3LmZhY2Vib29rL2xvZ2luIC0tZmlsZT1GYWNlYm9vawotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpweXRob24gZ2V0LWNvZGUucHkgLS1MSU5LIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9sb2dpbiAtLUZJTEU9RmFjZWJvb2sKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KWytdIG91dHB1dAp5b3UgY2FuIHRhcCBscyBpbiB5b3VyIHRlcm1pbmFsIHRvIGNoZWNrIHRoZSBmaWxlIG91dHB1dHRlZAp0aGUgcmVzdWx0cyB3aWxsIGJlIEZhY2Vib29rLmh0bWwKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIiIiKQojZGVmaW5lIHRoZSBvcHRpb25zCm9wdGlvbi5hZGRfb3B0aW9uKCctbCcsJy0tbGluaycsJy0tTCcsJy0tTElOSycsZGVzdD0ndXJsJyxoZWxwPXNtcy5sb3dlcigpLHR5cGU9c3RyLGRlZmF1bHQ9VHJ1ZSxtZXRhdmFyPSJ1cmwiKQpvcHRpb24uYWRkX29wdGlvbignLWYnLCctLWZpbGUnLCctLUYnLCctLUZJTEUnLGRlc3Q9J2ZpbGUnLHR5cGU9c3RyLGhlbHA9c21zMS5sb3dlcigpLGRlZmF1bHQ9VHJ1ZSxtZXRhdmFyPSJmaWxlbmFtZSIpCihvcHRpb25zLCBhcmdzKSA9IG9wdGlvbi5wYXJzZV9hcmdzKCkKdXJsID0gb3B0aW9ucy51cmwKZmlsZSA9IG9wdGlvbnMuZmlsZQp0cnk6CiAgICBodHRwcyA9IHVybC5zdGFydHN3aXRoKCdodHRwczovLycpCiAgICBodHRwID0gdXJsLnN0YXJ0c3dpdGgoJ2h0dHA6Ly8nKQogICAgd2hpbGUgVHJ1ZToKICAgICAgICBpZiBodHRwcyA9PSBUcnVlOgogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgICAgICBwcmludCgiXDAzM1sxOzMybXRoYW5rcyBmb3IgZHJvcHBpbmcgdGhlIHRhcmdldCB3ZWJzaXRlIHdpdGggcHJvdG9jb2whLFxuIHlvdSBpcyBzYXZlZCBhbmQgbmFtZWQge30iIC5mb3JtYXQoZmlsZSArIi5odG1sIikpCiAgICAgICAgICAgIGJyZWFrCiAgICAgICAgZWxpZiBodHRwID09IFRydWU6CiAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgICAgIHByaW50KCJcMDMzWzA7MzJtdGhhbmtzIGZvciBkcm9wcGluZyB0aGUgdGFyZ2V0IHdlYnNpdGUgd2l0aCBwcm90b2NvbCEsXG4geW91IGZpbGUgaXMgc2F2ZWQgYW5kIG5hbWVkIHt9IiAuZm9ybWF0KGZpbGUgKyIuaHRtbCIpKQogICAgICAgICAgICBicmVhawogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHRpbWUuc2xlZXAoMikKICAgICAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgICAgIHByaW50KCJcMDMzWzA7MzFtdHJ5IHRvIGVudGVyIHRoZSBwcm90b2NvbCBvZiB0aGUgdGFyZ2V0IHdlYnNpdGUgbGlrZSBodHRwczovLyBvciBodHRwOi8vIikKICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgc3lzLmV4aXQoNCkKICAgICAgICAjc3RhcnQgdG8gYnJvd3NpbmcKICAgIHJlID0gcmVxdWVzdHMuZ2V0KHVybCkKICAgIHJfY29kZSA9IHJlLnN0YXR1c19jb2RlCiAgICB3cml0ZXIgPSByZS50ZXh0CiAgICBpZiByX2NvZGUgPT0gMjAwOgogICAgICAgICAgICB3ZmlsZSA9IG9wZW4oZmlsZSsiLmh0bWwiLCAiYSsiKQogICAgICAgICAgICB3ZmlsZS53cml0ZSh3cml0ZXIpCiAgICAgICAgICAgIHdmaWxlLmNsb3NlKCkKICAgIGVsaWYgcl9jb2RlICE9IDIwMDoKICAgICAgICAgICAgdGltZS5zbGVlcCgzKQogICAgICAgICAgICBwcmludCgiXDAzM1sxOzMxbUFjY2VzcyBkZW5pZWQhIikKICAgICAgICAgICAgdGltZS5zbGVlcCg0KQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgdGltZS5zbGVlcCgwLjUpCiAgICBwcmludCgiXDAzM1sxOzMybURvbmUhIGJ5ZSEiKQpleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3IgYXMgZToKICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICBwcmludCAoIlwwMzNbMTszMW1bfl0iKyIgY2hlY2sgeW91ciBpbnRlcm5ldCBjb25uZWN0aW9uISIrIlwwMzNbMG0iKQpleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5JbnZhbGlkU2NoZW1hIGFzIHg6CiAgICB0aW1lLnNsZWVwKDEpCiAgICBwcmludCgiXDAzM1sxOzMzbXlvdSBoYXZlIGVudGVyZWQgSW52YWxpZCB1cmwgYnJvISIpCmV4Y2VwdCByZXF1ZXN0cy5leGNlcHRpb25zLkludmFsaWRVUkwgYXMgbzoKICAgIHByaW50KCJJbnZhbGlkIFVSTCB7fSIgLmZvcm1hdCh1cmwpKQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjIE1yIERlaCBINGNrM3IgIyMjIyMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjIEdFVC1DT0RFIHRvb2wgICMjIyMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw=="))
#end of tool
