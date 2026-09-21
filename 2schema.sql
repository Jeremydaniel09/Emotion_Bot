USE [project]
GO

/****** Object:  Table [dbo].[Emobot]    Script Date: 21/09/2026 10:07:10 pm ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Emobot](
	[Increment] [int] IDENTITY(1,1) NOT NULL,
	[UserID] [int] NOT NULL,
	[ChatroomID] [int] NOT NULL,
	[MessageContent] [nvarchar](max) NOT NULL,
	[Responder] [nvarchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


