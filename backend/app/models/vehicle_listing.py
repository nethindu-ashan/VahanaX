import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    Index,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class VehicleListing(Base):
    __tablename__ = "vehicle_listings"

    __table_args__ = (
        UniqueConstraint(
            "source",
            "source_listing_id",
            name="uq_vehicle_listings_source_listing_id",
        ),
        Index(
            "ix_vehicle_listings_freshness",
            "status",
            "first_seen_at",
        ),
        Index(
            "ix_vehicle_listings_search",
            "make",
            "model",
            "district",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Listing information
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Vehicle information
    vehicle_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    make: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    model_code: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    year: Mapped[int | None] = mapped_column(
        nullable=True,
        index=True,
    )

    # Price
    price: Mapped[Decimal | None] = mapped_column(
        Numeric(14, 2),
        nullable=True,
        index=True,
    )

    price_text: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="LKR",
    )

    # Location
    province: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    district: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        index=True,
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    area: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    latitude: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 6),
        nullable=True,
    )

    longitude: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 6),
        nullable=True,
    )

    # Source
    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    source_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    source_listing_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    source_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Seller
    seller_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    seller_phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    # Media
    image_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Processing
    advertisement_confidence: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 4),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="active",
        index=True,
    )

    # Freshness
    posted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    first_seen_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    # Internal timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )