# Require an explicit Paper target

Every `$paper-openspec` run requires a Paper file link from the latest request or unambiguous recent chat context. The workflow opens that exact file and passes its canonical file ID to every Paper operation that accepts `fileId` rather than trusting whichever file is active or recent, preventing otherwise valid design work from landing in the wrong file.
